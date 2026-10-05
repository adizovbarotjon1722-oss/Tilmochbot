FROM python:3.12-slim
# ffmpeg — ovoz uchun; tesseract — rasmdagi matnni o'qish uchun (o'zbek, ingliz, xitoy, rus)
RUN apt-get update && apt-get install -y --no-install-recommends \
        ffmpeg tesseract-ocr tesseract-ocr-uzb tesseract-ocr-eng tesseract-ocr-chi-sim tesseract-ocr-rus \
    && rm -rf /var/lib/apt/lists/*
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["python", "bot.py"]
