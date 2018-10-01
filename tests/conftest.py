from project import create_app
import pytest

from pymongo import MongoClient
from flask_pymongo import PyMongo

@pytest.fixture(scope='session')
def app():
    app = create_app()
    return app


@pytest.fixture(scope='session')
def mongo(request, app):
    # client = MongoClient('localhost:27017')

    mongo = PyMongo(app, uri='mongodb://localhost:27017/myTestDb')
    datab = mongo.db.myTestDb
    #db = me.connect('testdb', host='mongodb://localhost')
    yield datab
    datab.myTest
    datab.myTestb.drop()
    #mongo.close()