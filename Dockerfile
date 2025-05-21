FROM --platform=linux/amd64 python:3.12-slim

WORKDIR /app

RUN apt-get update && apt-get install -y gcc libpq-dev

COPY requirements.txt .
RUN pip install --upgrade pip && pip install Flask==3.1.0
RUN pip install -r requirements.txt

COPY . .

ENV FLASK_APP=flask_twitter_clone:create_app
ENV FLASK_ENV=development

EXPOSE 5000

CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
