__author__ = 'erik'

import os

basedir = os.path.abspath(os.path.dirname(__file__))

CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'
MONGODB_SETTINGS = {'DB': 'statistics', 'USERNAME': '', 'PASSWORD': '', 'HOST': 'mongodb', 'PORT': 27017}
