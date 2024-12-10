# Use the official Python image as a base
FROM python:3.10-slim-buster

# Install system dependencies including Tesseract
RUN apt-get update && \
apt-get -qq -y install tesseract-ocr && \
apt-get -qq -y install libtesseract-dev

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .


# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy your application code
COPY . .

# Command to run your application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]

