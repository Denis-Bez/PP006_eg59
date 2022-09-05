from flask_sqlalchemy import SQLAlchemy
from flask import Flask

db = SQLAlchemy()


# For creating tables need input that commands in Python's consol
# from extensions import create_app
# from Class_SQLAlchemy import *
# db.create_all(app=create_app())
def create_app():
    application = Flask(__name__)
    application.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///content.db'
    application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(application)

    return application
