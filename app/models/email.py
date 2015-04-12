__author__ = 'erik'
from app import db


class EmailConfirmation(db.Model):
    __tablename__ = 'email_confirmation'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    hash_c = db.Column(db.String)
    activation_time = db.Column(db.DateTime)
    requested_time = db.Column(db.DateTime)
    expiration_date = db.Column(db.DateTime, nullable=False)