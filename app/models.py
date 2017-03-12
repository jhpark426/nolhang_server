from datetime import datetime
from app import db

#플레이어정보
class Player(db.Model):
    __tablename__ = 'players'
    id = db.Column(db.String, primary_key=True)
    password = db.Column(db.String)
    gender = db.Column(db.String)
    achievement_rate = db.Column(db.Float)
    birth = db.Column(db.String)
    create_time = db.Column(db.DateTime, default=datetime.now)
    

class Profile(db.Model):
    __tablename__ = 'profiles'
    id = db.Column(db.Integer, primary_key=True)
    function_name = db.Column(db.String)
    execution_sec = db.Column(db.Float)
    create_time = db.Column(db.DateTime, default=datetime.now)
