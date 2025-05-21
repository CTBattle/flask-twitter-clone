from flask import Blueprint, request, jsonify
from flask_twitter_clone.models import db, Tweet, User, Like

tweets_bp = Blueprint("tweets", __name__, url_prefix="/tweets")

# Create tweet
@tweets_bp.route("/", methods=["POST"])
def create_tweet():
    data = request.get_json()
    content = data.get("content")
    user_id = data.get("user_id")

    if not content or not user_id:
        return jsonify({"error": "Missing content or user_id"}), 400

    user = User.query.get_or_404(user_id)
    tweet = Tweet(content=content, author=user)

    db.session.add(tweet)
    db.session.commit()

    return jsonify(tweet.to_dict()), 201

# List paginated tweets
@tweets_bp.route("/", methods=["GET"])
def list_tweets():
    page = request.args.get("page", 1, type=int)
    limit = request.args.get("limit", 10, type=int)

    tweets = Tweet.query.order_by(Tweet.created_at.desc()).paginate(page=page, per_page=limit, error_out=False)
    return jsonify({
        "tweets": [t.to_dict() for t in tweets.items],
        "total": tweets.total,
        "page": tweets.page,
        "pages": tweets.pages
    }), 200

# View a single tweet and increment view count
@tweets_bp.route("/<int:tweet_id>", methods=["GET"])
def get_tweet(tweet_id):
    tweet = Tweet.query.get_or_404(tweet_id)
    tweet.views += 1
    db.session.commit()
    return jsonify(tweet.to_dict()), 200

# Search tweets
@tweets_bp.route("/search", methods=["GET"])
def search_tweets():
    query = request.args.get("query", "")
    if not query:
        return jsonify({"error": "Query parameter required"}), 400

    tweets = Tweet.query.filter(Tweet.content.ilike(f"%{query}%")).all()
    return jsonify([t.to_dict() for t in tweets]), 200

# List top tweets by likes + views
@tweets_bp.route("/top", methods=["GET"])
def top_tweets():
    tweets = Tweet.query.order_by(Tweet.likes_count.desc(), Tweet.views.desc()).limit(10).all()
    return jsonify([t.to_dict() for t in tweets]), 200

# Like a tweet
@tweets_bp.route("/<int:tweet_id>/like", methods=["POST"])
def like_tweet(tweet_id):
    data = request.get_json()
    user_id = data.get("user_id")

    tweet = Tweet.query.get_or_404(tweet_id)
    user = User.query.get_or_404(user_id)

    existing_like = Like.query.filter_by(user_id=user.id, tweet_id=tweet.id).first()
    if existing_like:
        return jsonify({"message": "Already liked"}), 200

    like = Like(user_id=user.id, tweet_id=tweet.id)
    db.session.add(like)
    tweet.likes_count += 1
    db.session.commit()

    return jsonify({"message": "Liked"}), 200

# Unlike a tweet
@tweets_bp.route("/<int:tweet_id>/like", methods=["DELETE"])
def unlike_tweet(tweet_id):
    data = request.get_json()
    user_id = data.get("user_id")

    tweet = Tweet.query.get_or_404(tweet_id)
    user = User.query.get_or_404(user_id)

    like = Like.query.filter_by(user_id=user.id, tweet_id=tweet.id).first()
    if not like:
        return jsonify({"message": "Not liked"}), 200

    db.session.delete(like)
    tweet.likes_count = max(tweet.likes_count - 1, 0)
    db.session.commit()

    return jsonify({"message": "Unliked"}), 200
