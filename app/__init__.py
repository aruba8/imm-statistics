__author__ = 'erik'
from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from app.views.user_page_view import user_page

app = Flask(__name__, static_folder='static')
app.config.from_object('config')
app.register_blueprint(user_page)


lm = LoginManager()
lm.init_app(app)
lm.login_view = 'login'

db = SQLAlchemy(app)
from views import views
from app.models.user import User
from app.models.session import Session
from app.models.userdata import UserDataDB


