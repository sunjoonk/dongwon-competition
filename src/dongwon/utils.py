import re

def extract_json_from_response(text):
    match = re.search(r'```json\s*(\[.*\])\s*```', text, re.DOTALL)
    if match:
        return match.group(1)
    
    match = re.search(r'\[.*\]', text, re.DOTALL)
    if match:
        return match.group(0)
        
    return None

def sanitize_filename(name):
    return re.sub(r'[\\/*?:"<>|]', '_', name)