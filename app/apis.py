from flask import request
from flask_restful import Resource, Api
from sqlalchemy import or_, and_
from app import app
from .common import profiling, make_plain_dict
from .models import Player
from tornado.ioloop import IOLoop
import tornado.web
from json import dumps
from json import JSONEncoder

api = Api(app)

@app.route('/')
def hello_world():
    return 'Hello World!'

def test22():
    p = Player.query.filter(player_id == Player.id).first()
    player_pass = p.password
    player_gender = p.gender
    player_birth = p.birth
    player = make_plain_dict(p)
    return player

class PlayerCollection(Resource):
    @profiling
    def get(self, player_id):
        print("@@@@@@@@@@@@@@@@!!!!!!!!!!!!!!!!!!!!!!!!!")
        p = Player.query.filter(player_id == Player.id).first()
        player = make_plain_dict(p)
        print("여기는왓느냐")
        return player


class PlayerUnit(Resource):
    @profiling
    def get(self, player_id):
        if len(request.args) == 0: return "TEST-CASE", 204

        if request.args['platform'] == 'android':
            p = Player.query.filter(player_id == Player.id).first()

            if p is None: return "No such player", 204

            player_pass = p.password
            player_gender = p.gender
            player_birth = p.birth
            player = make_plain_dict(p)

            return player

            # position_row = Position.query.filter(Position.id == p.position_id).first()
            # complete_quest_count = Quest.query.filter(and_(Quest.player_id == int(player_id), Quest.status == "finish")).count()
            # ongoing_quest_count = Quest.query.filter(and_(Quest.player_id == int(player_id), Quest.status == "ongoing")).count()
            #
            # player = make_plain_dict(p)
            # player.update(add_prefix_to_dict("position", make_plain_dict(position_row)))
            # player['mission_total_count'] = Mission.query.filter().count()
            # player['complete_count'] = complete_quest_count
            # player['ongoing_quest_count'] = ongoing_quest_count

class Testing(Resource):
    @profiling
    def get(self):
        print("aaaaaaaaaa");
        return ;

api.add_resource(Testing, '/testing')
api.add_resource(PlayerCollection, '/players/<string:player_id>') #plural
