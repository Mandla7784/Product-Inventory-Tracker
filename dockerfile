FROM python:3.9
WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY inventory/ ./inventory/

# EXPOSE 8000

CMD ["python", "./inventory/main.py"]
