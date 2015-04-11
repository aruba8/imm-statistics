from app.models.user import User
from flask_wtf import Form
from wtforms.fields import StringField
from wtforms.validators import DataRequired, Email


class Forgot(Form):
    email = StringField('email', validators=[DataRequired(), Email()])
    
    def __init__(self, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)
        self.user = None

    def validate(self):
        rv = Form.validate(self)
        if not rv:
            return False

        user = User.query.filter_by(email=self.email.data).first()
        if user is None:
            self.email.errors.append("Couldn't find this email")
            return False

        self.user = user
        return True
