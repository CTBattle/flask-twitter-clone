from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Like(db.Model):
    __tablename__ = 'likes'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    tweet_id = db.Column(db.Integer, db.ForeignKey('tweets.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

    tweets = db.relationship('Tweet', backref='author', cascade="all, delete-orphan", lazy=True)
    liked_tweets = db.relationship('Tweet',
                                   secondary='likes',
                                   backref=db.backref('liked_by_users', lazy='dynamic'),
                                   lazy='dynamic')
    profile = db.relationship("UserProfile", back_populates="user", uselist=False)

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'tweets': [tweet.to_dict_basic() for tweet in self.tweets],
            'liked_tweets': [tweet.to_dict_basic() for tweet in self.liked_tweets],
            'profile': self.profile.to_dict() if self.profile else None
        }

class UserProfile(db.Model):
    __tablename__ = 'user_profiles'
    id = db.Column(db.Integer, primary_key=True)
    bio = db.Column(db.String(255))
    location = db.Column(db.String(100))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), unique=True)
    user = db.relationship("User", back_populates="profile")

    def to_dict(self):
        return {
            'bio': self.bio,
            'location': self.location
        }

class Tweet(db.Model):
    __tablename__ = 'tweets'
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    likes_count = db.Column(db.Integer, default=0)
    views = db.Column(db.Integer, default=0)

    def to_dict(self):
        return {
            'id': self.id,
            'content': self.content,
            'created_at': self.created_at.isoformat(),
            'likes_count': self.likes_count,
            'views': self.views,
            'author': {
                'id': self.author.id,
                'username': self.author.username
            },
            'liked_by_user_ids': [user.id for user in self.liked_by_users]
        }

    def to_dict_basic(self):
        return {
            'id': self.id,
            'content': self.content,
            'created_at': self.created_at.isoformat(),
        }
