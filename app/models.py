from app import app, db
from datetime import datetime



class Post(db.Model):
    post_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(35))
    phone = db.Column(db.String(14))
    email = db.Column(db.String(55))
    msg = db.Column(db.String(100))
    date_posted = db.Column(db.DateTime, default=datetime.now().date())
