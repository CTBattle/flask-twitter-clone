from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from flask_twitter_clone.models import db, User

auth_bp = Blueprint("auth", __name__, url_prefix="/auth")

@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return jsonify({"error": "Missing username or password"}), 400

    if User.query.filter_by(username=username).first():
        return jsonify({"error": "Username already exists"}), 400

    new_user = User(username=username)
    new_user.set_password(password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "User registered"}), 201

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    print("🔐 Login attempt:", username, password)  # Debug line

    if not username or not password:
        return jsonify({"error": "Missing username or password"}), 400

    user = User.query.filter_by(username=username).first()
    print("👤 Found user:", user)

    if not user:
        return jsonify({"error": "User not found"}), 404

    if not user.password_hash:
        return jsonify({"error": "No password hash set"}), 500

    if not user.check_password(password):
        return jsonify({"error": "Invalid credentials"}), 401

    access_token = create_access_token(identity=user.id)
    print("✅ Token created")
    return jsonify(access_token=access_token), 200

