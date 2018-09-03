from flask import Flask
from flask_cors import CORS

from api.api import api
from api.models import db


class Config(object):
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://tomabolt:password@192.168.99.100/sport_stats'
    SQLALCHEMY_TRACK_MODIFICATIONS = False



def create_app(config):
    app = Flask(__name__)
    CORS(app)
    app.config.from_object(config)
    register_extensions(app)
    return app


def register_extensions(app):
    api.init_app(app)
    db.init_app(app)
    pass


# Run the application
if __name__ == '__main__':
    app = create_app(Config)
    app.run(host='0.0.0.0', port=80, debug=True, threaded=True)
