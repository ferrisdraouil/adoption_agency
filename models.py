from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import expression

db = SQLAlchemy()


def connect_db(app):
    """Connect to SQLAlchemy"""
    db.app = app
    db.init_app(app)


class Pet(db.Model):
    """The pet class for SQL"""

    __tablename__ = 'pets'

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    species = db.Column(db.Text, nullable=False)
    photo_url = db.Column(db.Text, nullable=True)
    age = db.Column(db.Integer, nullable=False)
    notes = db.Column(db.Text, nullable=True)
    available = db.Column(
        db.Boolean, server_default=expression.true(), nullable=False)
