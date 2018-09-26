#create_app

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from project import models, routes
from .routes import web


def create_app(config=None):
    app = Flask(__name__)
    models.init_app(app)
    app.register_blueprint(web.web_bp)
    return app