import os
import logging
import warnings
from google import genai

# Suppress AFC console warnings
warnings.filterwarnings("ignore", category=UserWarning, module="google.genai")
logging.getLogger("google.genai").setLevel(logging.ERROR)

# Load key from environment or fallback to your key
API_KEY = os.environ.get("GEMINI_API_KEY", "AQ.Ab8RN6K_YFs71yb0h-GsZqu_OoLBTT4OK2xk745qpy4I--usZw")

client = genai.Client(api_key=API_KEY)
DEFAULT_MODEL = "gemini-flash-latest"