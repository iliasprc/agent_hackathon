import os
import json
import tempfile
from pathlib import Path
from dotenv import load_dotenv


load_dotenv()
GOOGLE_API_KEY: str = os.getenv("GOOGLE_API_KEY", "")
OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY")
GEMINI_MODEL : str = os.getenv("GEMINI_MODEL", "gemini-2.5-flash-lite")
GPT_MODEL : str = os.getenv("GPT_MODEL", "gpt-4o")