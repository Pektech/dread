#create_app
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from project import models, routes
from .routes import web
from config import Config
from flask_pymongo import PyMongo


config = {
    "dev": "config.DevConfig",
    "testing": "config.TestConfig",
    "default": "config.DevConfig"
        }
config_name = os.getenv('FLASK_ENV', 'default')



def create_app():
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    if os.getenv('FLASK_ENV') == 'testing':
        mongo = PyMongo(app=app, uri='mongodb://localhost:27017/myDatabase')
    # models.init_app(app)
    # mongo = PyMongo(app)
    app.register_blueprint(web.web_bp)
    return app