import numpy as np

def apply_holiday_gift_set_boost(product_name, monthly_sales, logger):
    TARGET_PRODUCTS = ['동원참치액 순 500g', '동원참치액 진 500g', '동원참치액 순 900g', '동원참치액 진 900g']
    
    GIFT_SALES_CONFIG = {
        '동원참치액 순 500g': {
            'feb_pre_sales': int(np.random.uniform(30000, 33000)),
            'sep_pre_sales': int(np.random.uniform(30000, 33000)),
            'feb_sales': int(np.random.uniform(100000, 110000)),
            'sep_sales': int(np.random.uniform(100000, 110000))
        },
        '동원참치액 진 500g': {
            'feb_pre_sales': int(np.random.uniform(30000, 33000)),
            'sep_pre_sales': int(np.random.uniform(30000, 33000)),
            'feb_sales': int(np.random.uniform(100000, 110000)),
            'sep_sales': int(np.random.uniform(100000, 110000))
        },
        '동원참치액 순 900g': {
            'feb_pre_sales': int(np.random.uniform(20000, 22000)),
            'sep_pre_sales': int(np.random.uniform(20000, 22000)),
            'feb_sales': int(np.random.uniform(60000, 66000)),
            'sep_sales': int(np.random.uniform(60000, 66000))
        },
        '동원참치액 진 900g': {
            'feb_pre_sales': int(np.random.uniform(20000, 22000)),
            'sep_pre_sales': int(np.random.uniform(20000, 22000)),
            'feb_sales': int(np.random.uniform(60000, 66000)),
            'sep_sales': int(np.random.uniform(60000, 66000))
        }
    }

    target_key = None
    for key in TARGET_PRODUCTS:
        if key in product_name:
            target_key = key
            break

    if not target_key:
        return monthly_sales
        
    logger.info(f"--- '{product_name}'에 대한 명절 선물세트 판매량 추가 시작 ---")
    
    sep_pre_index = 1
    sep_index = 2
    feb_pre_index = 6
    feb_index = 7
    
    sep_pre_boost = GIFT_SALES_CONFIG[target_key]['sep_pre_sales']
    original_sales = monthly_sales[sep_pre_index]
    monthly_sales[sep_pre_index] += sep_pre_boost
    logger.info(f" - 8월(추석 전): 판매량 {sep_pre_boost}개 추가. (기존: {original_sales} -> 변경: {monthly_sales[sep_pre_index]})")

    sep_boost = GIFT_SALES_CONFIG[target_key]['sep_sales']
    original_sales = monthly_sales[sep_index]
    monthly_sales[sep_index] += sep_boost
    logger.info(f" - 9월(추석): 판매량 {sep_boost}개 추가. (기존: {original_sales} -> 변경: {monthly_sales[sep_index]})")
    
    feb_pre_boost = GIFT_SALES_CONFIG[target_key]['feb_pre_sales']
    original_sales = monthly_sales[feb_pre_index]
    monthly_sales[feb_pre_index] += feb_pre_boost
    logger.info(f" - 1월(설 전): 판매량 {feb_pre_boost}개 추가. (기존: {original_sales} -> 변경: {monthly_sales[feb_pre_index]})")

    feb_boost = GIFT_SALES_CONFIG[target_key]['feb_sales']
    original_sales = monthly_sales[feb_index]
    monthly_sales[feb_index] += feb_boost
    logger.info(f" - 2월(설): 판매량 {feb_boost}개 추가. (기존: {original_sales} -> 변경: {monthly_sales[feb_index]})")

    return monthly_sales

def format_sales_numbers(product_name, monthly_sales, logger):
    rounding_base = 0
    rule_desc = "규칙 없음"

    if any(keyword in product_name for keyword in ['리챔 오믈레햄', '동원참치액 순', '동원참치액 진', '소화가 잘되는 우유로 만든 ']):
        rounding_base = 1000
        rule_desc = "100의 자리에서 반올림 (1000 단위)"
    elif any(keyword in product_name for keyword in ['동원맛참', '덴마크 하이그릭요거트']):
        rounding_base = 500
        rule_desc = "500 단위로 반올림"
    elif '프리미엄 동원참치액' in product_name:
        rounding_base = 200
        rule_desc = "200 단위로 반올림"

    if rounding_base > 0:
        formatted_sales = [int(round(sale / rounding_base) * rounding_base) for sale in monthly_sales]
        logger.info(f" - [숫자 정리] '{rule_desc}' 규칙을 적용합니다.")
        return formatted_sales
    else:
        return monthly_sales