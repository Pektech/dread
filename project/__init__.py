#create_app
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from project import models, routes
from .routes import web

from config import Config





config = {
    "dev": "config.DevConfig",
    "testing": "config.TestConfig",
    "default": "config.DevConfig"
        }
config_name = os.getenv('FLASK_ENV', 'default')



def create_app():

    app = Flask(__name__)
    app.config.from_object(config[config_name])

    from project.database import mongo
    mongo.init_app(app)
    app.register_blueprint(web.web_bp)
    from project import models, routes
    return app

