# Use official Python image
FROM python:3.9

# Set working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy inventory and test folders, and main.py
COPY inventory/ ./inventory/
COPY main.py ./main.py

# Expose port if needed (optional)
# EXPOSE 8000

# Run the application
CMD ["python", "./inventory/main.py"]
