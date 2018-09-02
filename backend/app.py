import json

from flask import Flask, jsonify
from flask_cors import CORS
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy

# Instantiate the app
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base, DeclarativeMeta
from sqlalchemy.orm import sessionmaker

app = Flask(__name__)
CORS(app)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql+psycopg2://tomabolt:password@192.168.99.100/sport_stats"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
db = SQLAlchemy(app)

Base = declarative_base()

Session = sessionmaker(bind=engine, autoflush=False)

def to_dict(obj):
    if isinstance(obj.__class__, DeclarativeMeta):
        # an SQLAlchemy class
        fields = {}
        for field in [x for x in dir(obj) if not x.startswith('_') and x != 'metadata']:
            data = obj.__getattribute__(field)
            try:
                json.dumps(data) # this will fail on non-encodable values, like other classes
                fields[field] = data
            except TypeError:
                fields[field] = None
        # a json-encodable dict
        return fields

class Player(Base):
    __tablename__ = 'players'
    firstname = db.Column(db.String(100), nullable=False, primary_key=True)
    lastname = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return '<Player %r>' % self.lastname


class Product(Resource):
    def get(self):
        sess = Session()
        return jsonify([to_dict(player) for player in sess.query(Player).all()])


# Create routes
api.add_resource(Product, '/')

# Run the application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True, threaded=True)
