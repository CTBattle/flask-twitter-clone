from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from dotenv import load_dotenv

load_dotenv()

from .models import db
from .users import bp as users_bp
from .tweets import bp as tweets_bp

def create_app():
    app = Flask(__name__)
    
    # ✅ Save the SQLite database in the root of the project directory
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///twitter.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)
    Migrate(app, db)
    CORS(app)

    app.register_blueprint(users_bp, url_prefix="/users")
    app.register_blueprint(tweets_bp, url_prefix="/tweets")

    @app.route("/")
    def index():
        return {"message": "Welcome to the Twitter Clone API!"}, 200

    return app
