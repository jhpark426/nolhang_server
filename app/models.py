#-*- coding: utf-8 -*-
from datetime import datetime
from app import db
import sqlalchemy
from sqlalchemy.types import Integer, String, Unicode
#플레이어정보
####################################################3

class Player(db.Model):
	__tablename__='players'
	id=db.Column(db.Integer,primary_key=True)
	name=db.Column(db.String(64))
	gender=db.Column(db.String(64))
	age=db.Column(db.Integer)
	tel=db.Column(db.Integer)
	solve_question_count=db.Column(db.Integer)
	create_time=db.Column(db.DateTime,default=datetime.now)

	player=db.relationship('Inventory',backref='post',cascade='all,delete-orphan',lazy='dynamic')

class Profile(db.Model):
	__tablename__='profiles'
	id=db.Column(db.Integer,primary_key=True)
	function_name=db.Column(db.String(64))
	execution_sec=db.Column(db.Float)
	create_time=db.Column(db.DateTime,default=datetime.now)

class Region(db.Model):
	__tablename__='regions'
	region_code=db.Column(db.Integer,primary_key=True)
	region_name=db.Column(db.String(64))
	question=db.relationship('Question',backref='post',cascade='all,delete-orphan',lazy='dynamic')

class Question(db.Model):
	__tablename__='questions'
	question_code=db.Column(db.Integer,primary_key=True)
	region_code=db.Column(db.Integer,db.ForeignKey("regions.region_code"))
	question=db.Column(db.String)
	answer=db.Column(db.String)
	content_type=db.Column(db.String)


class Inventory(db.Model):
	__tablename__="inventory"
	index=db.Column(db.Integer,primary_key=True)
	player_code=db.Column(db.String(64),db.ForeignKey('players.id'))
	question_code=db.Column(db.String(64))
	status=db.Column(db.String(64),default=0)
	start_time=db.Column(db.DateTime,default=datetime.now)
	finish_teim=db.Column(db.DateTime,default=datetime.now)
