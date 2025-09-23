
FROM python:3.9

# Set working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt


# Copy inventory folder (contains main.py)
COPY inventory/ ./inventory/


# EXPOSE 8000

# Run the application
CMD ["python", "./inventory/main.py"]
