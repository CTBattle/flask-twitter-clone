FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Copy all files into the container
COPY . /app

# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Set environment variables
ENV FLASK_APP=flask_twitter_clone
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_ENV=development

# Expose the port Flask runs on
EXPOSE 5000

# Run the Flask app
CMD ["flask", "run"]
