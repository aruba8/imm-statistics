__author__ = 'erik'
from app import dbm


class User(dbm.Document):
    username = dbm.StringField(max_length=80, min_length=3, unique=True)
    password = dbm.StringField()
    active = dbm.BooleanField()

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

