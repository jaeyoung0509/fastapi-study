FROM python:3.8-slim

# Set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1 

# 컨테이너 내에서 코드가 실행될 경로 설정
WORKDIR /usr/src/app
# requirements.txt에 명시된 필요한 packages 설치
COPY requirements.txt ./
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8000
