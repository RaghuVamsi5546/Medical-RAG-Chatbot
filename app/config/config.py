import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
HF_TOKEN = os.getenv("HF_TOKEN")
GROQ_MODEL_NAME = "openai/gpt-oss-20b"
DB_FAISS_PATH = Path("vectorstore/db_faiss")
DATA_PATH = Path("data/")
CHUNK_SIZE = 500
CHUNK_OVERLAP = 50
