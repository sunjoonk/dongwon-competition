import os
import re
import json
import logging

class PersonaCache:
    def __init__(self, cache_dir):
        self.cache_dir = cache_dir
        os.makedirs(self.cache_dir, exist_ok=True)
        self.logger = logging.getLogger(__name__)

    def load_personas(self, product_name):
        safe_product_name = self.sanitize_filename(product_name)
        cache_file_path = os.path.join(self.cache_dir, f'{safe_product_name}_personas.json')
        
        if os.path.exists(cache_file_path):
            try:
                with open(cache_file_path, 'r', encoding='utf-8') as f:
                    personas = json.load(f)
                self.logger.info(f"Loaded {len(personas)} personas from cache for '{product_name}'.")
                return personas
            except Exception as e:
                self.logger.error(f"Error loading personas from cache: {e}")
        
        self.logger.warning(f"No cache found for '{product_name}'.")
        return []

    def save_personas(self, product_name, personas):
        safe_product_name = self.sanitize_filename(product_name)
        cache_file_path = os.path.join(self.cache_dir, f'{safe_product_name}_personas.json')
        
        try:
            with open(cache_file_path, 'w', encoding='utf-8') as f:
                json.dump(personas, f, ensure_ascii=False, indent=4)
            self.logger.info(f"Saved {len(personas)} personas to cache for '{product_name}'.")
        except Exception as e:
            self.logger.error(f"Error saving personas to cache: {e}")

    @staticmethod
    def sanitize_filename(name):
        return re.sub(r'[\\/*?:"<>|]', '_', name)