__author__ = 'erik'
from flask_wtf import Form
from wtforms.fields import StringField, PasswordField
from wtforms.validators import DataRequired


class LoginForm(Form):
    login = StringField('username', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])

