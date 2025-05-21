from flask import Blueprint, request, jsonify
from flask_twitter_clone.models import db, User, UserProfile

users_bp = Blueprint("users", __name__, url_prefix="/users")

# Create new user and auto-create profile
@users_bp.route("/", methods=["POST"])
def create_user():
    data = request.get_json()
    username = data.get("username")

    if not username:
        return jsonify({"error": "Username is required"}), 400

    if User.query.filter_by(username=username).first():
        return jsonify({"error": "Username already exists"}), 400

    user = User(username=username)
    user.profile = UserProfile(bio="", location="")

    db.session.add(user)
    db.session.commit()

    return jsonify(user.to_dict()), 201

# List all users
@users_bp.route("/", methods=["GET"])
def list_users():
    users = User.query.all()
    return jsonify([u.to_dict() for u in users]), 200

# Get one user
@users_bp.route("/<int:user_id>", methods=["GET"])
def get_user(user_id):
    user = User.query.get_or_404(user_id)
    return jsonify(user.to_dict()), 200

# Get user profile
@users_bp.route("/<int:user_id>/profile", methods=["GET"])
def get_profile(user_id):
    user = User.query.get_or_404(user_id)
    if not user.profile:
        return jsonify({"error": "Profile not found"}), 404
    return jsonify(user.profile.to_dict()), 200

# Update user profile
@users_bp.route("/<int:user_id>/profile", methods=["PATCH"])
def update_profile(user_id):
    user = User.query.get_or_404(user_id)
    data = request.get_json()

    if not user.profile:
        return jsonify({"error": "Profile not found"}), 404

    user.profile.bio = data.get("bio", user.profile.bio)
    user.profile.location = data.get("location", user.profile.location)

    db.session.commit()
    return jsonify(user.profile.to_dict()), 200
