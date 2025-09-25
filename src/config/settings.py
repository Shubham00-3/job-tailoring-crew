import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

SERPER_API_KEY = os.getenv("SERPER_API_KEY", "")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "llama3.1:8b-instruct")
