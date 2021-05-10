from flask import Flask
from flask_migrate import migrate	
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import marshmallow
from authz.contig import Config

db = SQLAlChemy()
ma = Marshmallow
mg = Migrate()
api = Api()

from authz import resource

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config) # Load confips from env variables.
    ma.init_app(app)
    db.init_app(app)
    mg.init_app(app, db)
    api. init_app(app)
    return app 

