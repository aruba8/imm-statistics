__author__ = 'erik'
from app import dbm


class Session(dbm.Document):
    username = dbm.StringField()