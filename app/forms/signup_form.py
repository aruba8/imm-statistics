__author__ = 'erik'
from flask_wtf import Form
from wtforms.fields import StringField, PasswordField, SelectField
from wtforms.validators import DataRequired
from app.models.userdata import COUNTRIES
from pycountry import countries


def create_countries_dict():
    country_dict = []
    for country in COUNTRIES:
        country_dict.append((country, countries.get(alpha2=country).name))
    return country_dict


class SignUpForm(Form):
    login = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm = PasswordField('Confirm')
    country = SelectField(choices=create_countries_dict())


