from config import client, DEFAULT_MODEL

def explain_concept(topic: str) -> str:
    try:
        prompt = f"""Explain the following concept to a student with zero background knowledge.

Structure:
1. **The Big Idea**: One clear sentence summary.
2. **Everyday Analogy**: Relate the concept to a common daily situation or object.
3. **How It Works**: 3 easy-to-digest bullet points.
4. **Why It Matters**: Brief real-world significance.

Concept:
{topic}"""

        response = client.models.generate_content(
            model=DEFAULT_MODEL,
            contents=prompt,
        )
        return response.text.strip() if response.text else "No explanation generated."
    except Exception as e:
        return f"Error explaining concept: {e}"