from flask import Blueprint, request, jsonify
from .models import db, Tweet, Like, User
from datetime import datetime
from sqlalchemy import func

bp = Blueprint("tweets", __name__)

@bp.route("/", methods=["GET"])
def get_all_tweets():
    page = request.args.get("page", 1, type=int)
    per_page = request.args.get("per_page", 10, type=int)

    tweets = Tweet.query.paginate(page=page, per_page=per_page, error_out=False)

    return jsonify({
        "tweets": [tweet.to_dict() for tweet in tweets.items],
        "total": tweets.total,
        "pages": tweets.pages,
        "current_page": tweets.page
    }), 200

@bp.route("/<int:tweet_id>", methods=["GET"])
def get_tweet(tweet_id):
    tweet = Tweet.query.get(tweet_id)
    if not tweet:
        return jsonify({"error": "Tweet not found"}), 404
    return jsonify(tweet.to_dict()), 200

@bp.route("/", methods=["POST"])
def create_tweet():
    data = request.get_json()
    if not data or "content" not in data or "user_id" not in data:
        return jsonify({"error": "Missing required fields"}), 400
    new_tweet = Tweet(content=data["content"], user_id=data["user_id"])
    db.session.add(new_tweet)
    db.session.commit()
    return jsonify(new_tweet.to_dict()), 201

@bp.route("/<int:tweet_id>", methods=["PUT"])
def update_tweet(tweet_id):
    tweet = Tweet.query.get(tweet_id)
    if not tweet:
        return jsonify({"error": "Tweet not found"}), 404
    data = request.get_json()
    tweet.content = data.get("content", tweet.content)
    db.session.commit()
    return jsonify(tweet.to_dict()), 200

@bp.route("/<int:tweet_id>", methods=["DELETE"])
def delete_tweet(tweet_id):
    tweet = Tweet.query.get(tweet_id)
    if not tweet:
        return jsonify({"error": "Tweet not found"}), 404
    db.session.delete(tweet)
    db.session.commit()
    return jsonify({"message": "Tweet deleted"}), 200

@bp.route("/<int:tweet_id>/like", methods=["POST"])
def like_tweet(tweet_id):
    data = request.get_json()
    user_id = data.get("user_id")
    if not user_id:
        return jsonify({"error": "Missing user_id"}), 400
    existing_like = Like.query.filter_by(user_id=user_id, tweet_id=tweet_id).first()
    if existing_like:
        return jsonify({"message": "Tweet already liked"}), 200
    new_like = Like(user_id=user_id, tweet_id=tweet_id, created_at=datetime.utcnow())
    tweet = Tweet.query.get(tweet_id)
    tweet.likes_count += 1
    db.session.add(new_like)
    db.session.commit()
    return jsonify({"message": "Tweet liked"}), 201

@bp.route("/<int:tweet_id>/unlike", methods=["POST"])
def unlike_tweet(tweet_id):
    data = request.get_json()
    user_id = data.get("user_id")
    if not user_id:
        return jsonify({"error": "Missing user_id"}), 400
    like = Like.query.filter_by(user_id=user_id, tweet_id=tweet_id).first()
    if not like:
        return jsonify({"message": "Like not found"}), 404
    tweet = Tweet.query.get(tweet_id)
    if tweet.likes_count > 0:
        tweet.likes_count -= 1
    db.session.delete(like)
    db.session.commit()
    return jsonify({"message": "Tweet unliked"}), 200

@bp.route("/<int:tweet_id>/liked", methods=["GET"])
def check_if_liked(tweet_id):
    user_id = request.args.get("user_id")
    if not user_id:
        return jsonify({"error": "Missing user_id"}), 400
    like = Like.query.filter_by(user_id=user_id, tweet_id=tweet_id).first()
    return jsonify({"liked": bool(like)}), 200

@bp.route("/search", methods=["GET"])
def search_tweets():
    keyword = request.args.get("q", "")
    if not keyword:
        return jsonify({"error": "Missing search query"}), 400
    results = Tweet.query.filter(Tweet.content.ilike(f"%{keyword}%")).all()
    return jsonify([tweet.to_dict() for tweet in results]), 200

@bp.route("/stats", methods=["GET"])
def tweet_stats():
    avg_likes = db.session.query(func.avg(Tweet.likes_count)).scalar()
    max_views = db.session.query(func.max(Tweet.views)).scalar()
    return jsonify({
        "average_likes": round(avg_likes or 0, 2),
        "max_views": max_views or 0
    }), 200

tweets_bp = bp
