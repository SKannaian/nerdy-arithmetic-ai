"""
Nerdy Arithmetic AI — Cloud Function 2nd Gen
Production deployment for Firebase / Google Cloud Functions
"""

import os
import re
import json
import functions_framework
from google import genai
from google.genai import types

def add_cors_headers(response_headers):
    response_headers["Access-Control-Allow-Origin"] = "*"
    response_headers["Access-Control-Allow-Methods"] = "GET, POST, OPTIONS"
    response_headers["Access-Control-Allow-Headers"] = "Content-Type, Authorization"
    return response_headers

def classify_cognitive_misconception(equation: str, expected: str, user_val_str: str, tier: str) -> dict:
    diagnosis = {
        "label": "Thinking It Through",
        "heuristic_hint": "Let's count the items step by step on our visual manipulative!",
        "emoji": "🧩"
    }

    try:
        user_val = float(user_val_str.strip())
        exp_val = float(expected.strip())
        diff = user_val - exp_val
        abs_diff = abs(diff)
    except Exception:
        return diagnosis

    nums = [float(n) for n in re.findall(r'\d+', equation)]
    
    if abs_diff == 1:
        return {
            "label": "Off-by-One Counting Slip",
            "heuristic_hint": "You're so close—just 1 away! Touch and count the last dot on the ten-frame one more time.",
            "emoji": "🎯"
        }

    if len(nums) >= 2:
        n1, n2 = nums[0], nums[1]
        if '+' in equation and user_val == abs(n1 - n2):
            return {
                "label": "Operation Confusion",
                "heuristic_hint": "Look at the sign! It's a PLUS sign (+), which means we are putting groups together, not taking away.",
                "emoji": "➕"
            }
        elif '-' in equation and user_val == (n1 + n2):
            return {
                "label": "Operation Confusion",
                "heuristic_hint": "Check the sign! It's a MINUS sign (−), so we are taking items away from our starting group.",
                "emoji": "➖"
            }

    if abs_diff in (10, 9, 11):
        return {
            "label": "Place Value / Regrouping Slip",
            "heuristic_hint": "Check the tens column! Did you remember to bundle 10 ones into a new ten rod?",
            "emoji": "📦"
        }

    if user_val > exp_val:
        return {
            "label": "Answer Too High",
            "heuristic_hint": f"Your answer ({int(user_val)}) is a bit high. Try counting down or double-checking your tens!",
            "emoji": "🎈"
        }
    else:
        return {
            "label": "Answer Too Low",
            "heuristic_hint": f"Your answer ({int(user_val)}) is a little bit low. Double-check using our visual blocks!",
            "emoji": "🌱"
        }

@functions_framework.http
def health(request):
    if request.method == "OPTIONS":
        return ("", 204, add_cors_headers({}))
    
    key_set = bool(os.environ.get("GEMINI_API_KEY"))
    return (
        json.dumps({
            "status": "healthy",
            "service": "Nerdy Arithmetic AI Cloud Service",
            "gemini_api_key_set": key_set,
            "version": "2.0.0"
        }),
        200,
        add_cors_headers({"Content-Type": "application/json"})
    )

@functions_framework.http
def chat(request):
    if request.method == "OPTIONS":
        return ("", 204, add_cors_headers({}))

    try:
        data = request.get_json(silent=True) or {}
        equation = data.get("equation", "")
        expected = str(data.get("expected_answer", ""))
        user_val = str(data.get("user_answer") or data.get("user_message") or "")
        tier = data.get("tier", "k1")
        hint_level = data.get("hint_level", 1)

        misconception = classify_cognitive_misconception(equation, expected, user_val, tier)

        api_key = os.environ.get("GEMINI_API_KEY") or data.get("api_key")

        if not api_key:
            return (
                json.dumps({
                    "reply": f"🤖 **Byte (Math Mentor):** {misconception['heuristic_hint']}",
                    "cognitive_diagnosis": misconception["label"],
                    "encouragement_emoji": misconception["emoji"],
                    "source": "heuristic_fallback"
                }),
                200,
                add_cors_headers({"Content-Type": "application/json"})
            )

        client = genai.Client(api_key=api_key)

        tier_contexts = {
            "k1": "The student is in Kindergarten or 1st Grade (ages 5-7). Use simple, warm words, short sentences under 25 words, and concrete visual references like colored dots.",
            "23": "The student is in 2nd or 3rd Grade (ages 7-9). Guide them to think about place value (tens and ones), regrouping blocks, and number lines. Keep it under 35 words.",
            "45": "The student is in 4th or 5th Grade (ages 9-11). Encourage mental math, array grids, and factoring patterns. Keep it under 40 words."
        }

        system_instruction = f"""
You are "Byte", the cheerful, encouraging robotic math tutor on Nerdy Arithmetic AI.
Your golden rule: NEVER REVEAL OR SPOIL THE FINAL NUMERIC ANSWER DIRECTLY.
Guide them Socratic-style so they discover it themselves.

Grade Level Context:
{tier_contexts.get(tier, tier_contexts['k1'])}

Diagnostic Insight:
Our cognitive analyzer flagged: "{misconception['label']}".
Hint Level: Level {hint_level} of 3.
Tone: Enthusiastic, patient, supportive, uses 1 emoji.
"""

        prompt = f"""
Problem: {equation}
Expected Correct Answer: {expected}
Student Answer: {user_val}
Student Question: {data.get("user_message", "")}

Provide your Socratic response:
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
        
        # Anti-spoil safety
        if expected and expected in reply_text:
            reply_text = misconception["heuristic_hint"]

        return (
            json.dumps({
                "reply": f"🤖 **Byte:** {reply_text}",
                "cognitive_diagnosis": misconception["label"],
                "encouragement_emoji": misconception["emoji"],
                "source": "gemini-2.5-flash"
            }),
            200,
            add_cors_headers({"Content-Type": "application/json"})
        )

    except Exception as e:
        return (
            json.dumps({
                "reply": "🤖 **Byte:** Let's count the tokens together on the ten-frame above!",
                "cognitive_diagnosis": "Thinking It Through",
                "encouragement_emoji": "🧩",
                "source": "heuristic_fallback",
                "error": str(e)
            }),
            200,
            add_cors_headers({"Content-Type": "application/json"})
        )
