import os
from dotenv import load_dotenv

class Config:
    def __init__(self):
        load_dotenv()
        self.api_key = os.getenv("GEMINI_API_KEY")
        if not self.api_key:
            raise ValueError("GEMINI_API_KEY must be set in the environment variables.")
        self.use_api_to_generate_personas = False  # Default value, can be overridden

    def set_api_usage(self, use_api):
        self.use_api_to_generate_personas = use_api

config = Config()