from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS

from flask_twitter_clone.models import db
from flask_twitter_clone.users import users_bp
from flask_twitter_clone.tweets import tweets_bp

def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///twitter.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)
    Migrate(app, db)
    CORS(app)

    app.register_blueprint(users_bp)
    app.register_blueprint(tweets_bp)

    return app
