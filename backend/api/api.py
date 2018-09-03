from flask import jsonify
from flask_restful import Resource, Api

from .models import Session, to_dict, Player as PlayerModel


api = Api()

class Player(Resource):
    def get(self):
        sess = Session()
        return jsonify([to_dict(player) for player in sess.query(PlayerModel).all()])

api.add_resource(Player, '/')
