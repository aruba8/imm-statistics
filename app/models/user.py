__author__ = 'erik'
from app import db

ROLE_USER = 0
ROLE_ADMIN = 1


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(length=80), index=True, unique=True)
    password = db.Column(db.String())
    role = db.Column(db.SmallInteger, default=ROLE_USER)
    active = db.Column(db.Boolean())

    def is_authenticated(self):
        return True

    def is_active(self):
        return self.active

    def is_anonymous(self):
        return False

    def get_username(self):
        return str(self.username)

    def get_id(self):
        return str(self.username)

    def get_password(self):
        return str(self.password)

    def __unicode__(self):
        return self.username

    def __repr__(self):
        return '<User %r>' % self.username

