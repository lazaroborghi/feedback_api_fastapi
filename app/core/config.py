import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    MONGO_URI = os.getenv("MONGO_URI")
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

settings = Settings()

def get_database():
    from app.db.mongodb import MongoDB
    return MongoDB()

def get_ai_model():
    from app.ai.openai_model import OpenAIModel
    return OpenAIModel()
