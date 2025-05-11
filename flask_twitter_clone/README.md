# Flask Twitter Clone

A simple but powerful REST API built with Flask that mimics core Twitter features like posting tweets, liking/unliking, and managing users.

## 🔧 Features
- ✅ User registration and management
- 📝 Tweet creation, editing, and deletion
- ❤️ Like and unlike tweets
- 🔍 Search tweets by content
- 📊 Tweet statistics (avg likes, max views)
- 📁 SQLite database integration
- 🧩 Modular RESTful API architecture

## 🧰 Tech Stack
- Python 3.11
- Flask
- SQLAlchemy & Flask-Migrate
- Flask-CORS
- SQLite

## 🚀 Setup Instructions
1. Clone this repository
2. Install dependencies: `pip install -r flask_twitter_clone/requirements.txt`
3. Run migrations: `flask --app flask_twitter_clone db upgrade`
4. Seed the database: `./seed.sh`
5. Start the server: `./run.sh`
6. Open [http://localhost:5000](http://localhost:5000)

## 📌 Future Improvements
- 🔐 JWT authentication
- 📄 Pagination for tweets
- 👤 User profile bios
- 🧪 Unit testing and validation

## 📜 License
MIT License — free to use and extend.
