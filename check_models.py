from google import genai

API_KEY = "AQ.Ab8RN6K_YFs71yb0h-GsZqu_OoLBTT4OK2xk745qpy4I--usZw"

client = genai.Client(api_key=API_KEY)

print("Models available to your account:\n")
for model in client.models.list():
    # Only show models that support generating text
    if "generateContent" in getattr(model, "supported_actions", []):
        print(model.name)