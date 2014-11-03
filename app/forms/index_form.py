__author__ = 'erik'

from flask_wtf import Form
from wtforms.fields import SelectField
from app.utils.helper import EMBASSY_CITIES


def create_dict(source):
    return [(city, city) for city in source]


class FilterForm(Form):
    embassy = SelectField('Embassy', choices=create_dict(EMBASSY_CITIES), coerce=str, description='Answer the question')

