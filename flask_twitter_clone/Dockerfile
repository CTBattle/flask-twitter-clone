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
ENV FLASK_ENV=production

# Expose the port used by Flask, default to 5000
EXPOSE 5000

# Run the Flask app on the Railway-provided port or fallback to 5000
CMD ["flask", "run", "--host=0.0.0.0", "--port=${PORT:-5000}"]
