import os
import time
import logging
import warnings
from google import genai

warnings.filterwarnings("ignore", category=UserWarning, module="google.genai")
logging.getLogger("google.genai").setLevel(logging.ERROR)

API_KEY = os.environ.get("GEMINI_API_KEY", "AQ.Ab8RN6LN2FTYfgWxIW_7vo3LQAaUwaXaanrFK7plG5rRjo_F9Q")
client = genai.Client(api_key=API_KEY)

# Broad array of stable production endpoints to bypass server spikes
FALLBACK_MODELS = [
    "gemini-2.5-flash",
    "gemini-3.5-flash",
    "gemini-flash-latest",
]

def generate_with_fallback(prompt: str) -> str:
    last_error = None
    
    for model_name in FALLBACK_MODELS:
        # Retry loop per model (handles temporary 503 spikes gracefully)
        for attempt in range(2):
            try:
                response = client.models.generate_content(
                    model=model_name,
                    contents=prompt,
                )
                if response and response.text:
                    return response.text.strip()
            except Exception as e:
                last_error = e
                error_str = str(e)
                
                # If server is unavailable (503) or rate-limited (429/404), try backing off or switching models
                if "503" in error_str or "UNAVAILABLE" in error_str:
                    time.sleep(1.5)  # brief pause before retry/fallback
                    continue
                elif "429" in error_str or "RESOURCE_EXHAUSTED" in error_str or "404" in error_str:
                    break # Break out of attempt loop to jump to next model immediately
                else:
                    raise e
                    
    raise RuntimeError(f"All model endpoints are currently busy or unavailable. Please try again in a few moments. Details: {last_error}")