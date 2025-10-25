# Constants used throughout the application

PRODUCT_NAMES = [
    '동원맛참 고소참기름 135g',
    '동원맛참 고소참기름 90g',
    '동원맛참 매콤참기름 135g',
    '동원맛참 매콤참기름 90g',
    '동원참치액 순 500g',
    '동원참치액 순 900g',
    '동원참치액 진 500g',
    '동원참치액 진 900g',
    '프리미엄 동원참치액 500g',
    '프리미엄 동원참치액 900g',
    '덴마크 하이그릭요거트 400g',
    '리챔 오믈레햄 200g',
    '리챔 오믈레햄 340g',
    '소화가 잘되는 우유로 만든 바닐라라떼 250mL',
    '소화가 잘되는 우유로 만든 카페라떼 250mL'
]

INITIAL_ADOPTION_RATES = {
    'established': (0.45, 0.5),
    'new': (0.03, 0.05)
}

HOLIDAY_MONTHS = {
    'seol': [1, 2],  # January (pre-sales), February (sales)
    'chuseok': [8, 9]  # August (pre-sales), September (sales)
}

ROUNDING_RULES = {
    '1000': ['리챔 오믈레햄', '동원참치액 순', '동원참치액 진', '소화가 잘되는 우유로 만든 '],
    '500': ['동원맛참', '덴마크 하이그릭요거트'],
    '200': ['프리미엄 동원참치액']
}