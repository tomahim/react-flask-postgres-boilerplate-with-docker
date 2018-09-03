class Config(object):
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://tomabolt:password@192.168.99.100/sport_stats'
    SQLALCHEMY_TRACK_MODIFICATIONS = False