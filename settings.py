import os


class Config:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = f'sqlite:///db_{BASE_DIR.split("/")[-1]}.db'
    SECRET_KEY = 'your secret key'
