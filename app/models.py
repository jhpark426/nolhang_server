from datetime import datetime
from app import db

#플레이어정보

class Player(db.Model):
        __tablename__='players'
        id = db.Column(db.String,primary_key=True)
        name = db.Column(db.String)
        gender = db.Column(db.String)
        age = db.Column(db.Integer)
        tel = db.Column(db.Integer)
        solve_question_count = db.Column(db.Integer)
        create_time = db.Column(db.DateTime,default=datetime.now)

class Profile(db.Model):
    __tablename__ = 'profiles'
    id = db.Column(db.Integer, primary_key=True)
    function_name = db.Column(db.String)
    execution_sec = db.Column(db.Float)
    create_time = db.Column(db.DateTime, default=datetime.now)

class Region(db.Model):
        __talbename__ = 'regions'
        region_code = db.Column(db.Integer,primary_key=True)
        region_name = db.Column(db.String)

class Question(db.Model):
        __tablename__ = 'questions'
        question_code = db.Column(db.Integer,primary_key=True)
        region_code = db.Column(db.Integer,db.ForeignKey('regions.region_code'))
        question = db.Column(db.String)
        answer = db.Column(db.String)
        content_type = db.Column(db.String)

class Inventory(db.Model):
        __tablename__ = 'inventory'
        index = db.Column(db.Integer,primary_key=True)
        player_code = db.Column(db.Integer,db.ForeignKey('player.id'))
        question_code = db.Column(db.Integer)
        status = db.Column(db.Integer,default=0)
        start_time = db.Column(db.DateTime,default=datetime.now)
        finish_time = db.Column(db.DateTime,default=datetime.now)
