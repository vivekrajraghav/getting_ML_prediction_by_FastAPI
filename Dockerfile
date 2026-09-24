#Base image
FROM python:3.11-slim

# Set Directory
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

#Copy rest application
COPY . .

# Expose Application Port

EXPOSE 8000

# Command to start the FastAPI Application

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
