import os
import json
import logging
from .api import generate_personas_from_api, extract_json_from_response
from .prompt import create_product_specific_prompt
from .persona_cache import PersonaCache
from .utils import sanitize_filename

logger = logging.getLogger(__name__)

class PersonaGenerator:
    def __init__(self, config):
        """
        Initializes the PersonaGenerator.
        Args:
            config: Configuration object, expected to have a 'use_api' attribute.
        """
        # config에 use_api 설정이 없을 경우를 대비해 기본값 False 사용
        self.use_api = getattr(config, 'use_api', False) 
        self.cache = PersonaCache(cache_dir='personas')
        logger.info(f"PersonaGenerator initialized. API usage: {self.use_api}")

    def generate_personas(self, product_name, num_personas=30):
        """
        Generates or loads personas for a given product.
        - If use_api is False, it will try to load from cache first.
        - If use_api is True (or cache is empty), it will call the API and update the cache.
        """
        # API를 사용하지 않을 경우, 캐시에서 먼저 로드 시도
        if not self.use_api:
            personas = self.cache.load_personas(product_name)
            if personas:
                logger.info(f"Loaded {len(personas)} personas from cache for '{product_name}'.")
                return personas
        
        # API를 사용하거나 캐시가 비어있을 경우, 새로 생성
        logger.info(f"Generating new personas for '{product_name}' using API.")
        prompt = create_product_specific_prompt(product_name, num_personas)
        if not prompt:
            logger.error("Failed to create prompt. Aborting persona generation.")
            return []

        response_text = generate_personas_from_api(prompt)
        json_string = extract_json_from_response(response_text)
        personas = json.loads(json_string) if json_string else []

        if personas:
            self.cache.save_personas(product_name, personas)
        
        return personas