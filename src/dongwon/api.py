from dotenv import load_dotenv
import os
import re
import google.generativeai as genai
import logging

logger = logging.getLogger(__name__)

def configure_api():
    load_dotenv()
    api_key = os.getenv("GEMINI_API_KEY")
    
    if not api_key:
        logger.error("GEMINI_API_KEY is not set in the environment variables.")
        raise ValueError("API key is required for API interactions.")
    
    genai.configure(api_key=api_key)
    logger.info("Gemini API configured successfully.")

def generate_personas(prompt):
    try:
        response = genai.generate_content(prompt)
        return response
    except Exception as e:
        logger.error(f"Error generating personas: {e}")
        raise

def extract_json_from_response(response_text):
    match = re.search(r'```json\s*(\[.*\])\s*```', response_text, re.DOTALL)
    if match:
        return match.group(1)
    
    match = re.search(r'\[.*\]', response_text, re.DOTALL)
    if match:
        return match.group(0)
        
    return None