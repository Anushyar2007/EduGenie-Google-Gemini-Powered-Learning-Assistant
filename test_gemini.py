from google import genai

API_KEY = "AQ.Ab8RN6K_YFs71yb0h-GsZqu_OoLBTT4OK2xk745qpy4I--usZw"

client = genai.Client(api_key=API_KEY)

print("Contacting Gemini...")
response = client.models.generate_content(
    model="gemini-3.8-flash",
    contents="Explain gravity to a 7-year-old in two sentences.",
)

print("\nResponse:")
print(response.text)