import json
import re
from config import client, DEFAULT_MODEL

def clean_json_block(text: str) -> str:
    # Extracts the exact JSON array between the first '[' and last ']'
    match = re.search(r'\[.*\]', text, re.DOTALL)
    if match:
        return match.group(0).strip()
    
    # Fallback strip
    cleaned = re.sub(r"^```(?:json)?", "", text.strip(), flags=re.IGNORECASE)
    cleaned = re.sub(r"```$", "", cleaned.strip())
    return cleaned.strip()

def generate_quiz(text: str):
    try:
        prompt = f"""Generate exactly 3 multiple-choice questions (MCQs) testing comprehension of the passage below.
Each question must have 4 clear choices, with 1 unambiguous correct answer and an explanation.

Return ONLY a valid JSON array without any markdown fences, backticks, or extra text:
[
  {{
    "id": 1,
    "question": "Question text here?",
    "options": ["Choice A", "Choice B", "Choice C", "Choice D"],
    "answer": "Choice A",
    "explanation": "Brief explanation why this option is correct."
  }}
]

Passage:
{text}"""

        response = client.models.generate_content(
            model=DEFAULT_MODEL,
            contents=prompt,
        )
        cleaned = clean_json_block(response.text)
        data = json.loads(cleaned)
        return data
    except Exception as e:
        return [{"error": f"Failed to generate quiz: {e}"}]