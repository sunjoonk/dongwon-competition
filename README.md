# 동원 판매량 시뮬레이터

## 개요
**동원 판매량 시뮬레이터**는 고객 페르소나와 시장 역학을 기반으로 다양한 제품의 월별 판매량을 예측하는 시장 시뮬레이션 도구입니다. 생성형 AI(Google Gemini)를 활용하여 제품별 가상 고객(페르소나)을 동적으로 생성하고, 에이전트 기반 모델링을 통해 시장 확산 및 구매 행동을 시뮬레이션합니다.

## 주요 기능
- **AI 기반 페르소나 생성**: 제품 특성에 맞는 타겟 고객 프로필을 기반으로 AI가 가상 고객 페르소나를 자동 생성합니다.
- **시장 시뮬레이션**: 에이전트 기반 모델링과 Bass 확산 모델을 사용한 시장 행동 시뮬레이션
- **결과 후처리**: 명절 선물세트 판매량과 같은 현실적인 요소를 시뮬레이션 결과에 반영하고, 제품군 특성에 맞게 판매량을 보정합니다.
- **자동화된 전체 제품 예측**: 한 번의 실행으로 `constants.py`에 정의된 모든 제품의 12개월 판매량을 예측하고, 결과를 CSV 파일로 저장합니다.

## 프로젝트 구조
```
dongwon-competition/
├── src/
│   └── dongwon/
│       ├── __init__.py          # 패키지 초기화
│       ├── cli.py               # 시뮬레이션 실행을 위한 명령어 인터페이스(CLI)
│       ├── config.py            # 설정 관리(API 키 등)
│       ├── logger.py            # 로깅 설정
│       ├── api.py               # Google Gemini API 통신
│       ├── prompt.py            # AI에게 전달할 프롬프트 생성
│       ├── persona_generator.py # 페르소나 생성 및 캐시 관리
│       ├── persona_cache.py     # 생성된 페르소나를 파일로 저장/로드
│       ├── agents.py            # 가상 고객(에이전트) 클래스 정의
│       ├── simulation.py        # 시장 확산 및 구매 행동 시뮬레이션 로직
│       ├── postprocessing.py    # 시뮬레이션 결과 후처리
│       ├── utils.py             # 유틸리티 함수
│       └── constants.py         # 제품 목록, 시뮬레이션 상수 정의
├── data/                        # 데이터 파일
│   └── sample_submission.csv
├── personas/                    # 페르소나 캐시
│   └── .gitkeep
├── prompt_template.txt          # 프롬프트 템플릿
├── .env.example                 # 환경 변수 예시
├── pyproject.toml               # 프로젝트 메타데이터
└── README.md                    # 문서
```

## 설치 방법
1. 저장소 복제:
   ```
   git clone https://github.com/sunjoonk/dongwon-competition.git
   ```
2. 프로젝트 디렉토리로 이동:
   ```
   cd dongwon-competition
   ```
3. 필요한 의존성 설치:
   ```
   pip install -r requirements.txt
   ```

## 사용 방법
시뮬레이터를 실행하려면 명령줄 인터페이스를 사용하세요:
```
python -m src.dongwon.cli
```

## 환경 설정
- API 키 및 기타 설정을 위해 `.env.example` 파일을 기반으로 `.env` 파일을 생성하세요.

## 라이선스
이 프로젝트는 MIT 라이선스 하에 있습니다. 자세한 내용은 LICENSE 파일을 참조하세요.
