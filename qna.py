from config import client, DEFAULT_MODEL

def ask_question(question: str) -> str:
    try:
        prompt = f"""You are an expert tutor. Provide a well-structured, clear, and direct answer to the student's question below.
Use bolding for core terms, and bullet points or numbered steps where relevant.

Student Question:
{question}"""

        response = client.models.generate_content(
            model=DEFAULT_MODEL,
            contents=prompt,
        )
        return response.text.strip() if response.text else "No answer received."
    except Exception as e:
        return f"Error answering question: {e}"