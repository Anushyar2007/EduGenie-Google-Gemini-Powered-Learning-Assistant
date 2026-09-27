from config import client, DEFAULT_MODEL

def summarize_text(text: str) -> str:
    try:
        prompt = f"""You are an educational summarizer. Summarize the following educational text for a student.

Format your output using clean Markdown:
- **Core Summary**: 2-3 concise sentences capturing the main thesis.
- **Key Takeaways**: 3 to 5 clear bullet points highlighting essential facts.
- **Important Terms**: Key vocabulary or definitions introduced.

Text to summarize:
{text}"""

        response = client.models.generate_content(
            model=DEFAULT_MODEL,
            contents=prompt,
        )
        return response.text.strip() if response.text else "No summary could be generated."
    except Exception as e:
        return f"Error generating summary: {e}"