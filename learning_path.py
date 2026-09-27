from config import client, DEFAULT_MODEL

def get_learning_recommendations(topic: str) -> str:
    try:
        prompt = f"""Create an actionable, step-by-step learning roadmap for a student wanting to master: '{topic}'.

Format with Markdown:
### 1. Beginner Stage (Foundations)
- **Topics to Learn**: Key fundamentals
- **Milestone Project**: A beginner project to test skills
- **Estimated Time**: Hours/weeks

### 2. Intermediate Stage (Application)
- **Topics to Learn**: Advanced methods & tools
- **Milestone Project**: Practical real-world project

### 3. Advanced Stage (Mastery)
- **Topics to Learn**: Optimization, system design, or depth concepts
- **Recommended Free Resources**: Best documentation, platforms, or tools to explore."""

        response = client.models.generate_content(
            model=DEFAULT_MODEL,
            contents=prompt,
        )
        return response.text.strip() if response.text else "No roadmap generated."
    except Exception as e:
        return f"Error creating learning path: {e}"