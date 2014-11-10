
__author__ = 'erik'

from flask_wtf import Form
from wtforms.fields import SelectField, StringField
from app.utils.helper import EMBASSY_CITIES, INTERVIEW_CITIES, FILTER_CHOICES


def create_dict(source):
    return [(city, city) for city in source]


class FilterForm(Form):
    embassy = SelectField('Embassy', choices=create_dict(EMBASSY_CITIES), coerce=str)
    interview_location = SelectField('Interview location', choices=create_dict(INTERVIEW_CITIES), coerce=str)
    chooser = SelectField('Dates to filter', choices=FILTER_CHOICES, coerce=str)
    from_date = StringField()
    to_date = StringField()

