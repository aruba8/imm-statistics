__author__ = 'erik'

import hmac
import random
import string
import hashlib
from config import SECRET_KEY
from utils.logger import Logger

logger = Logger()
log = logger.get_logger()
from app.models.user import User
from app.models.session import Session as SessionModel
from app import db


class Sessions:
    def start_session(self, user_id):
        # session = {'username': user_id}
        try:
            SessionModel(username=user_id).save()
        except:
            log.error("Unexpected error on start_session:")
            return -1

    def validate_login(self, username, password):
        user = User.query.filter_by(username=username).first()
        if user is None:
            log.warn("User not in database")
            return False

        salt = user.password.split(',')[1]
        if user.password != self.make_pw_hash(password, salt):
            log.warn("user password is not a match")
            return False

        # looks good

        return True

    # implement the function make_pw_hash(name, pw) that returns a hashed password
    # of the format:
    # HASH(pw + salt),salt
    # use sha256

    def make_pw_hash(self, pw, salt=None):
        if salt is None:
            salt = self.make_salt()
        return hashlib.sha256(pw + salt).hexdigest() + "," + salt

    # makes a little salt
    def make_salt(self):
        salt = ""
        for i in range(5):
            salt = salt + random.choice(string.ascii_letters)
        return salt

    def check_secure_val(self, h):
        val = h.split('|')[0]
        if h == self.make_secure_val(val):
            return val

    def make_secure_val(self, s):
        return "%s|%s" % (s, self.hash_str(s))

    SECRET = SECRET_KEY

    def hash_str(self, s):
        return hmac.new(self.SECRET, s).hexdigest()

    # creates a new user in the database
    def new_user(self, username, email, password, _id=None):
        password_hash = self.make_pw_hash(password)

        try:
            user = User(username=username, email=email, password=password_hash, active=True)
            if _id is not None:
                user.id = _id
            db.session.add(user)
            db.session.commit()
        except Exception as e:
            log.error("oops, username: " + username + " is already taken")
            log.error(e)
            return False
        return True


    def validate_new_user(self, username, password, confirm):
        if username is None or username == '':
            return False
        if password != confirm:
            return False
        return True

    def make_hash_c(self, email):
        salt = self.make_salt()
        return hashlib.sha256(email + salt).hexdigest()

    def save(self, model):
        db.session.add(model)
        db.session.commit()

    def update_email_conf(self, email_conf_pre, email_conf):
        email_conf_pre.hash_c = email_conf.hash_c
        email_conf_pre.requested_time = email_conf.requested_time
        email_conf_pre.expiration_date = email_conf.expiration_date
        db.session.add(email_conf_pre)
        db.session.commit()

