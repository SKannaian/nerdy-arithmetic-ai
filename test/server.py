"""
Nerdy AI Hackathon Suite — Local Test Backend
Follows the proven architecture from Google Capstone Cyber-Quest Mentor:
- FastAPI local server
- Serves interactive HTML/JS frontends
- Bridges Socratic tutoring requests to Gemini models (gemini-2.5-flash / gemini-1.5-flash)
- Provides automatic Socratic fallback heuristics if offline or without an API key

Run:
    python server.py
Then open:
    http://localhost:8765
"""

import os
import sys
import json
from pathlib import Path
from typing import List, Optional

import uvicorn
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from dotenv import load_dotenv

# Load local environment variables
load_dotenv()

# Google GenAI SDK
GENAI_AVAILABLE = False
try:
    from google import genai
    from google.genai import types
    GENAI_AVAILABLE = True
    print("✅ google-genai SDK loaded successfully.")
except ImportError:
    print("⚠️ google-genai package not installed. Running in heuristic Socratic mode.")

app = FastAPI(title="Nerdy AI Hackathon Local Suite", version="1.0.0")

# CORS middleware for local testing
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# ── Data Models ─────────────────────────────────────────────────────────────
class Message(BaseModel):
    role: str  # "user" | "assistant" | "model"
    content: str

class ChatRequest(BaseModel):
    api_key: Optional[str] = None
    model: str = "gemini-2.5-flash"
    messages: List[Message] = []
    user_message: str
    system_instruction: Optional[str] = None
    tier: Optional[str] = "k1"
    equation: Optional[str] = None
    expected_answer: Optional[str] = None

class ChatResponse(BaseModel):
    reply: str
    source: str = "gemini"  # "gemini" | "heuristic_fallback"
    hint_ladder_level: int = 1

# ── Built-in Heuristic Socratic Engine (Zero-Crash Fallback) ─────────────────
def get_heuristic_socratic_hint(equation: str, expected_answer: str, user_answer: str, tier: str) -> str:
    """Generates intelligent pedagogical hints without spoiling the answer when offline."""
    try:
        user_val = float(user_answer.strip())
        exp_val = float(expected_answer.strip())
        diff = abs(user_val - exp_val)
    except Exception:
        return "Let's check our numbers together! Count each piece slowly or use the visual blocks above to double-check."

    if diff == 1:
        return "You are super close—just 1 step away! Check your counting fingers or dots one more time. What comes right next?"
    elif diff == 10:
        return "Check the tens place! Did we carry or borrow a ten, or maybe add one extra ten group?"
    elif user_val > exp_val:
        return f"Good try! Your answer ({int(user_val)}) is a little bit too high. Try working backwards or counting down."
    else:
        return f"Nice effort! Your answer ({int(user_val)}) is a little bit too small. Try adding up from the larger number."

# ── Endpoints ───────────────────────────────────────────────────────────────
@app.get("/health")
def health():
    key_configured = bool(os.environ.get("GEMINI_API_KEY"))
    return {
        "status": "healthy",
        "service": "Nerdy AI Hackathon Suite",
        "genai_sdk": GENAI_AVAILABLE,
        "gemini_api_key_set": key_configured
    }

@app.post("/chat", response_model=ChatResponse)
async def chat(req: ChatRequest):
    api_key = os.environ.get("GEMINI_API_KEY") or req.api_key
    
    # 1. Fallback heuristic if no API key or GenAI SDK missing
    if not api_key or not GENAI_AVAILABLE:
        hint = get_heuristic_socratic_hint(
            req.equation or "",
            req.expected_answer or "",
            req.user_message or "",
            req.tier or "k1"
        )
        return ChatResponse(
            reply=f"🤖 **Byte (Math Mentor):** {hint}",
            source="heuristic_fallback",
            hint_ladder_level=1
        )

    # 2. Invoke Gemini Live API
    try:
        client = genai.Client(api_key=api_key)
        
        system_instruction = req.system_instruction or (
            "You are 'Byte', a warm, encouraging robotic math companion for elementary school students. "
            "Your goal is Socratic coaching: NEVER give the student the final number directly. "
            "Instead, give a brief, enthusiastic 1-2 sentence guiding question using visual metaphors (apples, blocks, jumping frogs) "
            "tailored to the student's grade tier."
        )

        prompt = f"""
Student Grade Tier: {req.tier}
Problem: {req.equation}
Target Correct Answer: {req.expected_answer}
Student Answer: {req.user_message}

Diagnose their mistake and provide an encouraging Socratic question or visual hint to help them discover the answer themselves.
Keep it under 35 words. Use simple words and an emoji!
"""

        response = client.models.generate_content(
            model=req.model,
            contents=prompt,
            config=types.GenerateContentConfig(
                system_instruction=system_instruction,
                temperature=0.7,
                max_output_tokens=150
            )
        )
        
        reply_text = response.text.strip() if response and response.text else "Let's try counting the visual dots above!"
        return ChatResponse(
            reply=f"🤖 **Byte:** {reply_text}",
            source="gemini",
            hint_ladder_level=1
        )

    except Exception as e:
        print(f"[ERROR] Gemini API call failed: {e}")
        fallback = get_heuristic_socratic_hint(
            req.equation or "",
            req.expected_answer or "",
            req.user_message or "",
            req.tier or "k1"
        )
        return ChatResponse(
            reply=f"🤖 **Byte (Offline):** {fallback}",
            source="heuristic_fallback",
            hint_ladder_level=1
        )

# ── Serve Static Assets & UI ────────────────────────────────────────────────
static_dir = Path(__file__).parent
app.mount("/", StaticFiles(directory=str(static_dir), html=True), name="static")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8765))
    host = os.environ.get("HOST", "127.0.0.1")
    print(f"\n🚀 Nerdy AI Hackathon Suite running at: http://{host}:{port}\n")
    uvicorn.run(app, host=host, port=port)
