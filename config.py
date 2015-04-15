__author__ = 'erik'

import os

basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = False
TESTING = False

CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'
SQLALCHEMY_DATABASE_URI = 'postgresql://imm:imm@localhost:5432/imm_db'
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
RECAPTCHA_PUBLIC_KEY = '6LcRbv0SAAAAAKiwXd5lGAQrEvvMlVJ6xC1ZZyRl'
RECAPTCHA_PRIVATE_KEY = '6LcRbv0SAAAAAC9kGGqVNGHfVV-ErpbwkvhwsUsQ'
RECAPTCHA_OPTIONS = {'theme': 'white'}

MAIL_SERVER = 'smtp.googlemail.com'
MAIL_PORT = 465
MAIL_USE_SSL = True
MAIL_USE_TLS = False
MAIL_USERNAME = 'biomaks@gmail.com'
MAIL_PASSWORD = 'xxxxxx'
SERVER_NAME = 'localhost:5000'