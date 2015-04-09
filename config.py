__author__ = 'erik'

import os

basedir = os.path.abspath(os.path.dirname(__file__))

CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
RECAPTCHA_PUBLIC_KEY = '6LcRbv0SAAAAAKiwXd5lGAQrEvvMlVJ6xC1ZZyRl'
RECAPTCHA_PRIVATE_KEY = '6LcRbv0SAAAAAC9kGGqVNGHfVV-ErpbwkvhwsUsQ'
RECAPTCHA_OPTIONS = {'theme': 'white'}
RECAPTCHA = True