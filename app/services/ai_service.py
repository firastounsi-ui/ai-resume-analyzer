import os
import json
from typing import Optional

from dotenv import load_dotenv
from openai import OpenAI

from app.prompts import SYSTEM_PROMPT

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def analyze_resume(resume_text: str, job_description: Optional[str] = None):
    user_prompt = "Resume:\n" + resume_text.strip()

    if job_description:
        user_prompt += "\n\nJob Description:\n" + job_description.strip()

    response = client.responses.create(
        model="gpt-4.1-mini",
        input=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_prompt}
        ]
    )

    raw_output = response.output_text

    try:
        return json.loads(raw_output)
    except json.JSONDecodeError:
        return {
            "strengths": [],
            "weaknesses": ["AI response was not valid JSON"],
            "suggestions": ["Try again"],
            "match_summary": None,
            "match_score": None
        }
