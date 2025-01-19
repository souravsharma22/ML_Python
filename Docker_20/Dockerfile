FROM python:3.8-alpine

# Set working directory
WORKDIR /app

# Copy application code
COPY . /app

# Install Python dependencies
RUN pip install  -r requirments.txt

# Specify the default command to run the application
CMD ["python", "app.py"]
