__author__ = 'erik'
from app import db


class Session(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String())