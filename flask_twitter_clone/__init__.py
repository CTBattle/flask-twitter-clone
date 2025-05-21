import os
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from werkzeug.exceptions import HTTPException

from .models import db
from .users import users_bp
from .tweets import tweets_bp
from .auth import auth_bp  # Make sure you created auth.py

def create_app():
    app = Flask(__name__)

    # Config settings
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL", "sqlite:///twitter.db")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["JWT_SECRET_KEY"] = "super-secret-key"  # In production, use os.getenv("JWT_SECRET_KEY")

    # Extensions
    db.init_app(app)
    Migrate(app, db)
    CORS(app)
    JWTManager(app)

    # Blueprints
    app.register_blueprint(users_bp)
    app.register_blueprint(tweets_bp)
    app.register_blueprint(auth_bp)

    # Global error handler
    @app.errorhandler(Exception)
    def handle_exception(e):
        if isinstance(e, HTTPException):
            return e
        app.logger.error(f"Unhandled Exception: {e}", exc_info=True)
        return jsonify({"error": "Internal Server Error"}), 500

    return app
