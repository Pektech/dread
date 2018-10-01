import pytest
import os
from flask_pymongo import PyMongo

def test_connection(mongo):

    pek = {"greet" :"well hello"}
    mongo.greeting.insert_one(pek)
    query =  mongo.greeting.find({'greet' : 'well hello'})
    assert query[0]['greet'] =='well hello'



