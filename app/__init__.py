from flask import Flask
from flask_migrate import Migrate
from .extensions import database
from config import Config
from .models import *

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    database.init_app(app)
    # with app.app_context():
    #     migrate = Migrate(app, database)
    # migrate.init_app(app, database)
    return app