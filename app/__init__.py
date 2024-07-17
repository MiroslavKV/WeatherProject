import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase

from settings import Config

# init application of the Flask
app = Flask(__name__)
app.config.from_object(Config)


class Base(DeclarativeBase):
    pass


# configure the SQLite database, relative to the app instance folder
db = SQLAlchemy(model_class=Base)

# initialize the app with the extension
db.init_app(app)

from app.routes import *
