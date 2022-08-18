from flask_sqlalchemy import SQLAlchemy
from flask import Flask

db = SQLAlchemy()


# For creating tables need input that commands in Python's consol
# from extensions import create_app
# from Class_SQLAlchemy import *
# db.create_all(app=create_app())
def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///content.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    return app
