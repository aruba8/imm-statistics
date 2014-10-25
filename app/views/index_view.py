__author__ = 'erik'
from datetime import datetime

from flask import render_template, g
from app import app


@app.route('/')
@app.route('/index')
def index():
    user = g.user
    return render_template("index.html", user=user)


