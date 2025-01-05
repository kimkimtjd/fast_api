# 가상환경 생성
python -m venv fastapi-env

# 가상환경 활성화
# Windows
fastapi-env\Scripts\activate
# Mac/Linux
source fastapi-env/bin/activate

# 필요한 패키지 설치
pip install fastapi uvicorn

# requirements.txt 생성
pip freeze > requirements.txt
출처: https://coding-shop.tistory.com/377 [끄적끄적 코딩 공방:티스토리]