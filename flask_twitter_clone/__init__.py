from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from flask_jwt_extended import JWTManager

from flask_twitter_clone.models import db
from flask_twitter_clone.users import users_bp
from flask_twitter_clone.tweets import tweets_bp
from flask_twitter_clone.auth import auth_bp  # ⬅️ New JWT blueprint

def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///twitter.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["JWT_SECRET_KEY"] = "super-secret-key"  # 🔐 Replace in production

    db.init_app(app)
    Migrate(app, db)
    CORS(app)
    JWTManager(app)

    app.register_blueprint(users_bp)
    app.register_blueprint(tweets_bp)
    app.register_blueprint(auth_bp)  # ⬅️ Register /auth routes

    return app
