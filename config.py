__author__ = 'erik'

import os

basedir = os.path.abspath(os.path.dirname(__file__))

CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'
MONGODB_SETTINGS = {'DB': 'statistics', 'USERNAME': '', 'PASSWORD': '', 'HOST': 'mongodb', 'PORT': 27017}

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')