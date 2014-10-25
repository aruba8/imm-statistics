__author__ = 'erik'

from flask import redirect, render_template, request
from app import app

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")


