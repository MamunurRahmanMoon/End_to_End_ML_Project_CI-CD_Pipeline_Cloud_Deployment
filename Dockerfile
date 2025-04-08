# Use the official Python 3.11 image as the base image
FROM python:3.11-slim

# Set the working directory
WORKDIR /app

# Copy the rest of the application code
COPY . /app

# Install system dependencies
RUN apt update -y && apt install awscli -y 

# Install Python dependencies
RUN pip install -r requirements.txt

# Specify the command to run the application
CMD ["python3", "app.py"]
