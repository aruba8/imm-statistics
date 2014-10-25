__author__ = 'erik'
from flask import g
from flask_login import current_user
from datetime import datetime

from app import app
import index_view
import login_view

@app.before_request
def before_request():
    g.user = current_user
    if g.user.is_authenticated():
        g.user.last_seen = datetime.utcnow()

