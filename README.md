# Flask Twitter Clone

A lightweight Twitter-style REST API built with Flask, SQLAlchemy, and SQLite. This project demonstrates user accounts, tweet management, likes, search, pagination, and basic profiles — all built using best practices and deployed live on Railway.

---

## Live Demo

Deployed App: https://flask-twitter-clone-production-<your-id>.up.railway.app

---

## Screenshots

Coming soon — add Postman screenshots or live endpoint results.

---

## Features

### User Endpoints
- Create, update, delete, and fetch users
- View user profile info (bio and location)

### Tweet Endpoints
- Post, edit, delete, and fetch tweets
- Search tweets by keyword
- Paginate tweets for scalable performance

### Likes
- Like and unlike tweets
- View tweet stats: average likes, max views

---

## Technologies Used

- Backend: Python 3.11, Flask
- ORM: SQLAlchemy
- Migrations: Flask-Migrate
- Database: SQLite (local), Railway (cloud deployment)
- API Testing: Postman
- Version Control: Git and GitHub
- Deployment: Railway

---
## Project Structure

```
flask_twitter_clone/
├── __init__.py
├── models.py
├── users.py
├── tweets.py
├── run.sh
├── requirements.txt
├── Procfile
└── migrations/
```
---

## Setup Instructions

1. Clone the repo
```bash
git clone https://github.com/CTBattle/flask-twitter-clone.git
cd flask-twitter-clone
```

2. Create and activate a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Run the app
```bash
chmod +x run.sh
./run.sh
```

5. Test in browser or Postman
```bash
Example: http://localhost:5000/users
```
