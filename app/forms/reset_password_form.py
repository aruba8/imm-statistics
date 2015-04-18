from flask_wtf import Form
from wtforms.fields import PasswordField
from wtforms.validators import DataRequired, EqualTo, Length


class ResetPassword(Form):
    password = PasswordField('Password', validators=[DataRequired(), Length(min=7, max=80)])
    password_confirm = PasswordField('Confirm password',
                                     validators=[DataRequired(), EqualTo('password', message='Passwords must match')])