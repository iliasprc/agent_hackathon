import os
import json
import tempfile
from pathlib import Path
from dotenv import load_dotenv


load_dotenv()
GOOGLE_API_KEY: str = os.getenv("GOOGLE_API_KEY", "")
OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY")