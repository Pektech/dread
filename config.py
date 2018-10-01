import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'monkey-keeps-the-secret'
    # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
    #                           'sqlite:///' + os.path.join(basedir,
    #                                                       'messages.db')
    # SQLALCHEMY_TRACK_MODIFICATIONS = False
    FLASK_DEBUG=0
    DEBUG = False
    MONGO_URI = 'mongodb://localhost:27017/myProdDB'




class DevConfig(Config):
    FLASK_DEBUG = 0
    DEBUG = True
    MONGO_URI = 'mongodb://localhost:27017/myDevDB'


class TestConfig(Config):
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir,
    #                                                       'test_db.db')
    MONGO_URI = 'mongodb://localhost:27017/myTestDB'
    TESTING = True
    DEBUG = True
    ASK_VERIFY_REQUESTS = False