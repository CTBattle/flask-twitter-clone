# Flask Twitter Clone API

A full-featured Twitter-style backend API built with Flask, SQLAlchemy, and Flask-Migrate.  
Includes user accounts, tweets, likes, profiles, search, pagination, and top tweet logic.

---

## Features

### ✅ Core Functionality (Current Version)

- Create users  
- Auto-generated user profiles (bio and location)  
- Create, view, and list tweets  
- Like and unlike tweets  
- Tweet view counter (auto-increments on GET)  
- Search tweets by keyword  
- List top tweets by likes and views  
- Paginated tweet listing  
- List users with bio preview and tweet count  

---

### 🔧 Additional Features Explored in Previous Builds

> These were implemented or partially tested in earlier versions and may be reintroduced.

- Update and delete users  
- Edit and delete tweets  
- Unique username validation and error handling  
- User profile update endpoints  
- Basic authentication strategy (in progress)  
- Deployment to Railway (past test version)  

---

## Tech Stack

- Python 3.11  
- Flask  
- SQLAlchemy  
- Flask-Migrate (Alembic)  
- SQLite (local)  
- Postman / Insomnia (API testing)  
- Git + GitHub for version control  

---

## Project Structure

flask_twitter_clone/
├── init.py # App factory
├── models.py # User, Tweet, Like, Profile models
├── users.py # /users routes
├── tweets.py # /tweets routes
├── migrations/ # DB migration files
└── twitter.db # Local DB


---

## API Usage

### 1. Create User

```http
POST /users/
Content-Type: application/json

{
  "username": "charles"
}

POST /tweets/
Content-Type: application/json

{
  "content": "Hello world!",
  "user_id": 1
}

GET /tweets/1

POST /tweets/1/like
{
  "user_id": 1
}

DELETE /tweets/1/like
{
  "user_id": 1
}

GET /tweets/search?query=word
GET /tweets/top

GET /users/

# Install dependencies
pip install flask flask_sqlalchemy flask_migrate flask_cors

# Initialize database
flask --app flask_twitter_clone:create_app db init
flask --app flask_twitter_clone:create_app db migrate -m "initial"
flask --app flask_twitter_clone:create_app db upgrade

# Start the app
flask --app flask_twitter_clone:create_app run --debug

Deployment

This project was previously tested on Railway. Deployment instructions are ready for:

Railway
Render
Fly.io or Replit

Screenshots of API test results in Insomnia or Postman can be added here to show successful requests.

Future Enhancements

User login and token-based authentication (Flask-Login or JWT)
Tweet editing and soft deletion
Comments and retweets
Follow/follower logic
Render deployment with persistent DB

Author

Charles Battle
Nucamp Portfolio Project – Week 4 (Flask & SQL)
May 2025


---

Once this is added, commit it:

```bash
git add README.md
git commit -m "Final full README with fixed formatting and features"
git push
