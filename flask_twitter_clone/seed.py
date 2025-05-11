from flask_twitter_clone.app import create_app
from flask_twitter_clone.models import db, User, Tweet

app = create_app()

with app.app_context():
    db.drop_all()
    db.create_all()

    user1 = User(username="charles", password="pass123")
    user2 = User(username="guest", password="guest123")

    db.session.add_all([user1, user2])
    db.session.commit()

    tweet1 = Tweet(content="Welcome to Flask Twitter Clone!", user_id=user1.id)
    tweet2 = Tweet(content="Guest account tweeting in!", user_id=user2.id)

    db.session.add_all([tweet1, tweet2])
    db.session.commit()

    print("✅ Database seeded with initial data.")
