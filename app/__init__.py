__author__ = 'erik'
from flask import Flask
from flask_login import LoginManager
from flask_mongoengine import MongoEngine
from app.views.user_page_view import user_page

app = Flask(__name__, static_folder='static')
app.config.from_object('config')
app.register_blueprint(user_page)

dbm = MongoEngine(app)

lm = LoginManager()
lm.init_app(app)
lm.login_view = 'login'

from app.views import views

