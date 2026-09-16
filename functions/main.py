"""
Nerdy AI Hackathon Suite — Cloud Function 2nd Gen
Production deployment for Firebase / GCP Cloud Functions
"""

import os
import json
import functions_framework
from google import genai
from google.genai import types

def add_cors_headers(response_headers):
    response_headers["Access-Control-Allow-Origin"] = "*"
    response_headers["Access-Control-Allow-Methods"] = "GET, POST, OPTIONS"
    response_headers["Access-Control-Allow-Headers"] = "Content-Type, Authorization"
    return response_headers

@functions_framework.http
def health(request):
    if request.method == "OPTIONS":
        return ("", 204, add_cors_headers({}))
    
    key_set = bool(os.environ.get("GEMINI_API_KEY"))
    return (
        json.dumps({"status": "healthy", "service": "Nerdy AI Hackathon Suite", "gemini_api_key_set": key_set}),
        200,
        add_cors_headers({"Content-Type": "application/json"})
    )

@functions_framework.http
def chat(request):
    if request.method == "OPTIONS":
        return ("", 204, add_cors_headers({}))

    try:
        data = request.get_json(silent=True) or {}
        api_key = os.environ.get("GEMINI_API_KEY") or data.get("api_key")

        if not api_key:
            return (
                json.dumps({"reply": "🤖 **Byte:** Let's practice with the visual counters above!"}),
                200,
                add_cors_headers({"Content-Type": "application/json"})
            )

        client = genai.Client(api_key=api_key)
        tier = data.get("tier", "k1")
        equation = data.get("equation", "")
        expected = data.get("expected_answer", "")
        user_val = data.get("user_message", "")

        prompt = f"""
Student Grade Tier: {tier}
Problem: {equation}
Target Correct Answer: {expected}
Student Answer: {user_val}

Diagnose their mistake and provide an encouraging Socratic question or visual hint to help them discover the answer themselves.
Keep it under 35 words. Use simple words and an emoji!
"""

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
            config=types.GenerateContentConfig(
                system_instruction="You are Byte, a warm Socratic math companion for elementary school students. Never reveal the final number directly.",
                temperature=0.7,
                max_output_tokens=150
            )
        )

        reply_text = response.text.strip() if response and response.text else "Let's count the dots together!"
        return (
            json.dumps({"reply": f"🤖 **Byte:** {reply_text}", "source": "gemini"}),
            200,
            add_cors_headers({"Content-Type": "application/json"})
        )

    except Exception as e:
        return (
            json.dumps({"reply": f"🤖 **Byte (Offline):** Check the visual ten-frame dots above to double-check!", "error": str(e)}),
            200,
            add_cors_headers({"Content-Type": "application/json"})
        )
