class Config(object):
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://myuser:mypassword@192.168.99.100/sport_stats'
    SQLALCHEMY_TRACK_MODIFICATIONS = False