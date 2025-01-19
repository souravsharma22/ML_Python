FROM python:3.8-alpine

# Set working directory
WORKDIR /code

ENV FLASK_APP=app.py

ENV FLASK_RUN_HOST=0.0.0.0

# Copy application code
COPY . .

# Install Python dependencies
RUN pip install  -r requirment.txt

EXPOSE 5000
# Specify the default command to run the application
CMD ["flask", "run"]
