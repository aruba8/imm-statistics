__author__ = 'erik'

from app import db


class Reset(db.Model):
    __tablename__ = 'reset'
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    uuid = db.Column(db.String(length=80))
    expiration_date = db.Column(db.DateTime)