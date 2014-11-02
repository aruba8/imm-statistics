__author__ = 'erik'
from datetime import datetime

from flask import render_template, g
from app import app
from app.models.userdata import UserDataDB, UserDataView


@app.route('/')
@app.route('/index')
def index():
    user_data_objects = UserDataDB.objects
    users = [UserDataView(user) for user in user_data_objects]
    return render_template("index.html", user_data_objects=users)


