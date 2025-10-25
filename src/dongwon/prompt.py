import os
import logging

# 이 파일(prompt.py)의 위치를 기준으로 프로젝트 루트 디렉토리 경로를 설정합니다.
# (src/dongwon/ -> src/ -> project_root)
PATH = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
logger = logging.getLogger(__name__)

def create_product_specific_prompt(product_name, num_personas=30):
    target_customer_profile = "일반적인 대한민국 소비자"

    if '하이그릭요거트' in product_name:
        target_customer_profile = "20-40 대 여성으로, 건강과 자기관리에 관심이 많고, 소득 수준은 중상 이상인 1인 가구, 주로 온라인 채널을 통해 건강식품을 구매하는 경향이 있음."
    elif '맛참' in product_name:
        target_customer_profile = "20-40대 남녀로, 편의성과 새로운 맛을 추구하며 유튜브, 인스타그램 등 소셜 미디어에 익숙하고 편의점이나 온라인에서 간편하게 식사를 해결하려는 1인 가구 학생 및 직장인. 30-50대 주부로, 3인 이상 가구의 식사를 책임지고 있음. 대형마트에서 장을 보며, 명절 등 특별한 날에 가족을 위한 요리를 준비하는 것을 중요하게 생각함."
        if '매콤' in product_name:
            target_customer_profile += " 특히 매운맛을 선호하는 경향이 뚜렷함."
    elif '리챔' in product_name:
        target_customer_profile = "30-50대 주부로, 3인 이상 가구의 식사를 책임지고 있음. 대형마트에서 장을 보며, 명절 등 특별한 날에 가족을 위한 요리를 준비하는 것을 중요하게 생각함."
    elif '참치액' in product_name:
        target_customer_profile = "요리에 관심이 많은 30-60대 주부 또는 1인 가구. 집밥을 선호하며, 음식의 깊은 맛을 내기 위한 조미료에 투자를 아끼지 않음. 대형마트와 온라인 채널을 모두 이용함."
        if '진' in product_name or '프리미엄' in product_name:
            target_customer_profile += " 특히 요리 실력이 뛰어나고, 소득 수준이 높아 프리미엄 제품을 선호하는 미식가적 성향을 보임."
    elif '소화가 잘되는' in product_name:
        target_customer_profile = "유당불내증이 있거나 소화 건강에 신경 쓰는 20-50대. 건강을 위해 일반 유제품 대신 락토프리 제품을 선택하며, 출근길이나 점심시간에 편의점에서 자주 구매함."
        if '바닐라라떼' in product_name:
            target_customer_profile += " 단맛을 선호하는 젊은 층의 비중이 상대적으로 높음."

    prompt_template_path = os.path.join(PATH, 'prompt_template.txt')
    
    try:
        with open(prompt_template_path, 'r', encoding='utf-8') as f:
            prompt_template = f.read()
        
        prompt = prompt_template.format(
            num_personas=num_personas,
            product_name=product_name,
            target_customer_profile=target_customer_profile
        )
        
    except FileNotFoundError:
        logger.error(f"프롬프트 템플릿 파일({prompt_template_path})을 찾을 수 없습니다.")
        return None 
    except Exception as e:
        logger.error(f"프롬프트 템플릿 파일 로드 중 오류 발생: {e}")
        return None

    return prompt