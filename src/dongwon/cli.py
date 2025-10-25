import argparse
import logging
import pandas as pd
import os
from dongwon.simulation import MarketSimulation
from dongwon.persona_generator import PersonaGenerator
from dongwon.postprocessing import apply_holiday_gift_set_boost, format_sales_numbers
from dongwon.config import load_config, get_project_root
from dongwon.constants import PRODUCT_NAMES, INITIAL_ADOPTION_RATES
from dongwon.utils import get_product_type

def main():
    # --- 1. 설정 및 로깅 초기화 ---
    config = load_config()
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    # --- 2. 명령줄 인자 처리 (출력 파일 경로 지정) ---
    parser = argparse.ArgumentParser(description="Dongwon Sales Simulator")
    parser.add_argument(
        '--output', 
        type=str, 
        default='submission.csv', 
        help='Path to the output CSV file.'
    )
    args = parser.parse_args()

    # --- 3. 시뮬레이션 실행 및 결과 저장 ---
    all_results = []
    persona_generator = PersonaGenerator(config)

    for product_name in PRODUCT_NAMES:
        logger.info(f"--- Starting simulation for: {product_name} ---")

        # 페르소나 생성
        personas = persona_generator.generate_personas(product_name)
        if not personas:
            logger.error(f"No personas for '{product_name}'. Skipping simulation.")
            all_results.append([product_name] + [0] * 12)
            continue

        # 제품 타입에 따른 초기 시장 점유율 설정
        product_type = get_product_type(product_name)
        initial_adoption_rate = INITIAL_ADOPTION_RATES[product_type]

        # 시장 시뮬레이션 실행
        simulation = MarketSimulation(personas, config, initial_adoption_rate)
        monthly_sales = simulation.run_simulation(months=12)

        # 결과 후처리
        boosted_sales = apply_holiday_gift_set_boost(product_name, monthly_sales, logger)
        formatted_sales = format_sales_numbers(product_name, boosted_sales, logger)
        
        all_results.append([product_name] + formatted_sales)
        logger.info(f"Finished simulation for: {product_name}. Forecast: {formatted_sales}\n")

    # --- 4. 최종 결과를 CSV 파일로 저장 ---
    columns = ['product_name'] + [f'month_{i+1}' for i in range(12)]
    df = pd.DataFrame(all_results, columns=columns)
    
    output_path = os.path.join(get_project_root(), args.output)
    df.to_csv(output_path, index=False)
    logger.info(f"All simulations complete. Results saved to '{output_path}'")

if __name__ == "__main__":
    main()