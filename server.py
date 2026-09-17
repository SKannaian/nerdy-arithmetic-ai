"""
Nerdy Arithmetic AI — Secure Socratic Backend
Pedagogy-First Math Copilot for Elementary Learners (K–5)

Features:
- FastAPI local / production server
- Serves the gamified interactive frontend
- Secure Google Gemini 2.5 Flash / 1.5 Flash integration (zero client-side key leaks)
- Cognitive misconception diagnosis (off-by-one, inverted operator, regrouping slip)
- Age-appropriate Socratic hint ladder (guarantees NO answer spoiling)
- Zero-crash heuristic fallback engine if offline or without API key
"""

import os
import sys
import re
from pathlib import Path
from typing import List, Optional

import uvicorn
from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, JSONResponse
from pydantic import BaseModel
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Google GenAI SDK loading
GENAI_AVAILABLE = False
try:
    from google import genai
    from google.genai import types
    GENAI_AVAILABLE = True
    print("✅ google-genai SDK loaded successfully.")
except ImportError:
    print("⚠️ google-genai package not installed. Running in heuristic Socratic mode.")

app = FastAPI(
    title="Nerdy Arithmetic AI Backend",
    description="Socratic Elementary Math Copilot API",
    version="2.0.0"
)

# Enable CORS for local testing and cross-origin requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ── Data Models ─────────────────────────────────────────────────────────────
class ChatMessage(BaseModel):
    role: str
    content: str

class SocraticRequest(BaseModel):
    user_message: str
    tier: Optional[str] = "k1"           # k1 | 23 | 45
    skill_title: Optional[str] = "Addition"
    equation: Optional[str] = ""
    expected_answer: Optional[str] = ""
    user_answer: Optional[str] = ""
    hint_level: Optional[int] = 1        # 1: Visual Metaphor, 2: Decompose, 3: Step-by-Step
    api_key: Optional[str] = None

class SocraticResponse(BaseModel):
    reply: str
    cognitive_diagnosis: str
    source: str                          # "gemini-2.5-flash" | "heuristic_fallback"
    hint_ladder_level: int
    encouragement_emoji: str

# ── Cognitive Misconception Classifier ───────────────────────────────────────
def classify_cognitive_misconception(equation: str, expected: str, user_val_str: str, tier: str) -> dict:
    """Diagnoses the underlying conceptual misunderstanding before prompting the model."""
    diagnosis = {
        "type": "conceptual_uncertainty",
        "label": "Thinking It Through",
        "heuristic_hint": "Let's count the items step by step on the visual manipulative!",
        "emoji": "🧩"
    }

    try:
        user_val = float(user_val_str.strip())
        exp_val = float(expected.strip())
        diff = user_val - exp_val
        abs_diff = abs(diff)
    except Exception:
        return diagnosis

    # Parse operands from equation if present (e.g., "7 + 5 = ?")
    nums = [float(n) for n in re.findall(r'\d+', equation)]
    
    # 1. Off-by-one counting error
    if abs_diff == 1:
        return {
            "type": "counting_slip",
            "label": "Off-by-One Counting Slip",
            "heuristic_hint": "You're so close—just 1 away! Touch and count the last dot on the ten-frame one more time.",
            "emoji": "🎯"
        }

    # 2. Inverted Operator (+ instead of -, or - instead of +)
    if len(nums) >= 2:
        n1, n2 = nums[0], nums[1]
        if '+' in equation and user_val == abs(n1 - n2):
            return {
                "type": "inverted_operator",
                "label": "Operation Confusion",
                "heuristic_hint": "Look at the sign! It's a PLUS sign (+), which means we are putting groups together, not taking away.",
                "emoji": "➕"
            }
        elif '-' in equation and user_val == (n1 + n2):
            return {
                "type": "inverted_operator",
                "label": "Operation Confusion",
                "heuristic_hint": "Check the sign! It's a MINUS sign (−), so we are taking items away from our starting group.",
                "emoji": "➖"
            }

    # 3. Base-10 Regrouping / Place-Value slip
    if abs_diff in (10, 9, 11):
        return {
            "type": "regrouping_slip",
            "label": "Place Value / Regrouping Slip",
            "heuristic_hint": "Check the tens column! Did you remember to bundle 10 ones into a new ten rod?",
            "emoji": "📦"
        }

    # 4. Multiplied instead of added, or vice-versa
    if len(nums) >= 2:
        n1, n2 = nums[0], nums[1]
        if '×' in equation and user_val == (n1 + n2):
            return {
                "type": "multiplication_as_addition",
                "label": "Repeated Addition Needed",
                "heuristic_hint": f"Remember, {int(n1)} × {int(n2)} means {int(n1)} groups of {int(n2)}, not just {int(n1)} + {int(n2)}!",
                "emoji": "✖️"
            }

    # 5. Magnitude guidance
    if user_val > exp_val:
        return {
            "type": "overshoot",
            "label": "Answer Too High",
            "heuristic_hint": f"Your answer ({int(user_val)}) is a bit too high. Try counting up from the larger number {int(max(nums)) if nums else ''}!",
            "emoji": "🎈"
        }
    else:
        return {
            "type": "undershoot",
            "label": "Answer Too Low",
            "heuristic_hint": f"Your answer ({int(user_val)}) is a little bit low. Double check using our visual blocks above!",
            "emoji": "🌱"
        }

# ── API Endpoints ───────────────────────────────────────────────────────────
@app.get("/health")
def health_check():
    key_set = bool(os.environ.get("GEMINI_API_KEY"))
    return {
        "status": "healthy",
        "service": "Nerdy Arithmetic AI Platform",
        "genai_sdk_loaded": GENAI_AVAILABLE,
        "gemini_api_key_configured": key_set,
        "version": "2.0.0"
    }

@app.post("/api/chat", response_model=SocraticResponse)
@app.post("/chat", response_model=SocraticResponse)
async def socratic_tutor_endpoint(req: SocraticRequest):
    """
    Main Socratic AI endpoint. Analyzes student work and generates age-appropriate
    hints without ever spoiling the final answer.
    """
    # 1. First, classify the cognitive mistake
    misconception = classify_cognitive_misconception(
        req.equation or "",
        req.expected_answer or "",
        req.user_answer or req.user_message or "",
        req.tier or "k1"
    )

    api_key = os.environ.get("GEMINI_API_KEY") or req.api_key

    # 2. Check if we have Gemini API credentials
    if not api_key or not GENAI_AVAILABLE:
        return SocraticResponse(
            reply=f"🤖 **Byte (Math Mentor):** {misconception['heuristic_hint']}",
            cognitive_diagnosis=misconception["label"],
            source="heuristic_fallback",
            hint_ladder_level=req.hint_level or 1,
            encouragement_emoji=misconception["emoji"]
        )

    # 3. Call Google Gemini 2.5 Flash with strict Socratic guardrails
    try:
        client = genai.Client(api_key=api_key)

        tier_instructions = {
            "k1": "The student is in Kindergarten or 1st Grade (ages 5-7). Use very simple, warm words, short sentences (under 25 words), and concrete visual references like colored dots, fingers, or apples.",
            "23": "The student is in 2nd or 3rd Grade (ages 7-9). Guide them to think about place value (tens and ones), regrouping blocks, and number line hops. Keep it under 35 words.",
            "45": "The student is in 4th or 5th Grade (ages 9-11). Encourage them with mental math strategies, array grids, and factoring patterns. Keep it concise and inspiring under 40 words."
        }

        grade_context = tier_instructions.get(req.tier or "k1", tier_instructions["k1"])

        system_instruction = f"""
You are "Byte", the cheerful, encouraging robotic math tutor on Nerdy Arithmetic AI.
Your golden rule: NEVER REVEAL OR SPOIL THE FINAL NUMERIC ANSWER DIRECTLY under any circumstances.
Instead, your mission is Socratic guidance: ask a guiding question or give a visual hint that empowers the child to figure it out themselves.

Grade Level Context:
{grade_context}

Diagnostic Insight:
Our cognitive analyzer flagged: "{misconception['label']}".
Hint Level Requested: Level {req.hint_level} of 3.
- Level 1: Point to the visual manipulative or general concept.
- Level 2: Guide decomposition (break numbers apart).
- Level 3: Give a clear step-by-step thinking path.

Tone: Enthusiastic, patient, supportive, uses 1 emoji.
"""

        prompt = f"""
Skill/Topic: {req.skill_title or 'Arithmetic'}
Problem: {req.equation}
Expected Correct Answer: {req.expected_answer}
Student Answer: {req.user_answer or req.user_message}
Student Question / Context: {req.user_message}

Provide your short Socratic response to the student:
"""

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
            config=types.GenerateContentConfig(
                system_instruction=system_instruction,
                temperature=0.7,
                max_output_tokens=150
            )
        )

        reply_text = response.text.strip() if response and response.text else misconception["heuristic_hint"]
        
        # Guardrail check: if model accidentally outputs the target answer, replace with heuristic
        if req.expected_answer and str(req.expected_answer).strip() in reply_text:
            reply_text = misconception["heuristic_hint"]

        return SocraticResponse(
            reply=f"🤖 **Byte:** {reply_text}",
            cognitive_diagnosis=misconception["label"],
            source="gemini-2.5-flash",
            hint_ladder_level=req.hint_level or 1,
            encouragement_emoji=misconception["emoji"]
        )

    except Exception as e:
        print(f"[WARN] Gemini API error: {e}. Falling back to heuristic engine.")
        return SocraticResponse(
            reply=f"🤖 **Byte:** {misconception['heuristic_hint']}",
            cognitive_diagnosis=misconception["label"],
            source="heuristic_fallback",
            hint_ladder_level=req.hint_level or 1,
            encouragement_emoji=misconception["emoji"]
        )

# ── Serve Static Assets ──────────────────────────────────────────────────────
static_dir = Path(__file__).parent
app.mount("/", StaticFiles(directory=str(static_dir), html=True), name="static")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8765))
    host = os.environ.get("HOST", "127.0.0.1")
    print(f"\n🚀 Nerdy Arithmetic AI running at: http://{host}:{port}")
    print(f"🌟 Gamified K–5 Socratic Math Experience Ready!\n")
    uvicorn.run(app, host=host, port=port)
