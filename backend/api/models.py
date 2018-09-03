import json

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base, DeclarativeMeta
from sqlalchemy.orm import sessionmaker
from .config import Config

db = SQLAlchemy()

Base = declarative_base()

engine = create_engine(Config.SQLALCHEMY_DATABASE_URI)

Session = sessionmaker(bind=engine, autoflush=False)

class Player(Base):
    __tablename__ = 'players'
    firstname = db.Column(db.String(100), nullable=False, primary_key=True)
    lastname = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return '<Player %r>' % self.firstname + ' ' + self.lastname

def to_dict(obj):
    if isinstance(obj.__class__, DeclarativeMeta):
        # an SQLAlchemy class
        fields = {}
        for field in [x for x in dir(obj) if not x.startswith('_') and x != 'metadata']:
            data = obj.__getattribute__(field)
            try:
                json.dumps(data)  # this will fail on non-encodable values, like other classes
                fields[field] = data
            except TypeError:
                fields[field] = None
        # a json-encodable dict
        return fields