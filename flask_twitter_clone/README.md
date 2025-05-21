# Flask Twitter Clone

This is a simple Twitter-style REST API built using Flask, SQLAlchemy, and JWT-based authentication. It supports user registration, login, profile retrieval, tweeting, and liking tweets.

## Features

- User registration with secure password hashing
- Login with JWT authentication
- Protected endpoints requiring JWT
- Create and fetch tweets
- Like and unlike tweets
- User profile with bio and location
- SQLite database with Alembic migrations

## Technologies Used

- Python 3.11
- Flask
- Flask SQLAlchemy
- Flask JWT Extended
- Flask Migrate
- SQLite (via SQLAlchemy ORM)

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/flask-twitter-clone.git
cd flask-twitter-clone

#2. Create Virtual Environment
python3 -m venv venv
source venv/bin/activate  # or `venv\Scripts\activate` on Windows

#3. Install Dependencies
pip install -r requirements.txt
#or
pip install Flask Flask-SQLAlchemy Flask-JWT-Extended Flask-Migrate

#4. Initialize Database
flask --app flask_twitter_clone db init
flask --app flask_twitter_clone db migrate -m "Initial migration"
flask --app flask_twitter_clone db upgrade

#5. Run the Server
flask --app flask_twitter_clone run

API Endpoints

Auth
POST /auth/register
{ "username": "test", "email": "test@example.com", "password": "123" }
POST /auth/login
{ "username": "test", "password": "123" }
GET /auth/me
Requires Bearer token
Tweets (future feature scope)
GET /tweets
POST /tweets
POST /tweets/<id>/like
Project Structure

flask_twitter_clone/
│
├── __init__.py          # Flask app factory
├── models.py            # SQLAlchemy models
├── auth.py              # Auth blueprint (register/login)
├── tweets.py            # (Optional) tweets blueprint
│
├── migrations/          # Alembic migration scripts
└── instance/twitter.db  # SQLite DB (auto-created)

Honors Project Bonus Features
✅ Added email + password hashing
✅ JWT authentication
✅ /auth/me protected route
✅ Cleaned migration history
✅ Deployed-ready structure

License

MIT License © 2025 Charles Battle