# src/config/llm.py
from langchain_ollama import ChatOllama   # <── instead of langchain_community
from src.config.settings import OLLAMA_MODEL

def get_llm(model: str | None = None, temperature: float = 0.2, num_ctx: int = 8192):
    return ChatOllama(
        model=model or OLLAMA_MODEL,
        temperature=temperature,
        num_ctx=num_ctx,
        base_url="http://localhost:11434"   # Ollama runs here by default
    )
