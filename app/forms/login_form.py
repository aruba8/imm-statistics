from app.models.user import User

__author__ = 'erik'
from flask_wtf import Form
from wtforms.fields import StringField, PasswordField
from wtforms.validators import DataRequired


class LoginForm(Form):
    login = StringField('username', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])

    def __init__(self, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)
        self.user = None

    def validate(self):
        rv = Form.validate(self)
        if not rv:
            return False

        user = User.query.filter_by(username=self.login.data).first()
        if user is None:
            self.login.errors.append('Unknown user')
            return False

        self.user = user
        return True

