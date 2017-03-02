from flask import request
from flask_restful import Resource, Api
from sqlalchemy import or_, and_
from app import app
from tornado.ioloop import IOLoop
import tornado.web

api = Api(app)

@app.route('/')
def hello_world():
    return 'Hello World!'
