from flask import jsonify
from flask_restful import Resource, Api

from .models import Player as PlayerModel, to_dict

api = Api()

class Player(Resource):
    def get(self):
        return jsonify([to_dict(player) for player in PlayerModel.query.all()])

api.add_resource(Player, '/')
