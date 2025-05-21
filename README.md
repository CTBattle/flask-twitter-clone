/Users/charlesbattle/Desktop/NucampFolder/Python/2-SQL/week4/README.md

# Flask Twitter Clone – Honors Project

This is a full-featured backend for a Twitter-style app built using **Flask**, **PostgreSQL**, and **Docker Compose**. Developed as an Honors Portfolio Project for Nucamp's backend course.

## Features
- User registration and hashed password storage
- User authentication
- Posting and viewing tweets
- Liking tweets
- Viewing profiles with bio/location
- Tracks tweet views
- RESTful API with clean endpoints

## Technologies
- Python 3.12
- Flask 3.1.0
- SQLAlchemy & Flask-Migrate
- PostgreSQL
- Docker & Docker Compose
- GitHub + Render (or Railway)

## API Endpoints

| Feature          | Method | Endpoint                  | Body (JSON) |
|------------------|--------|---------------------------|-------------|
| Create user      | POST   | `/users`                  | `{ "username", "email", "password" }` |
| Get users        | GET    | `/users` or `/users/<id>` | —           |
| Create tweet     | POST   | `/tweets`                 | `{ "content", "user_id" }` |
| View tweets      | GET    | `/tweets` or `/tweets/<id>` | —         |
| Like a tweet     | POST   | `/likes`                  | `{ "user_id", "tweet_id" }` |
| View tweet likes | GET    | `/tweets/<id>/likes`      | —           |
| View profile     | GET    | `/profiles/<user_id>`     | —           |
| Update profile   | PATCH  | `/profiles/<user_id>`     | `{ "bio", "location" }` |

## Setup Instructions

### Local
1. Clone the repo:
   ```bash
   git clone https://github.com/CTBattle/flask-twitter-clone.git
   cd flask-twitter-clone
```
DATABASE_URL=postgresql://postgres:password@db:5432/twitter_clone_db
```
```
docker-compose up --build
```
```
docker exec -it flask_container flask db upgrade
```
--

Cloud (Render / Railway)
Dockerfile and docker-compose.yml included
Flask runs on port 5000
Database runs in its own container
Folder Structure

/flask_twitter_clone
├── __init__.py
├── models.py
├── routes.py
└── ...

--

Author
Charles Battle — GitHub

Update README with project overview and instructions
