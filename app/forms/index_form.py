
__author__ = 'erik'

from flask_wtf import Form
from wtforms.fields import SelectField, StringField
from app.utils.helper import FILTER_CHOICES
from app.models.userdata import UserDataDB


def create_dict(source):
    list_ = [('', '')]
    for item in source:
        if item[0] == u'' or item[0] is None:
            pass
        else:
            list_.append((item[0], item[0]))
    return list_

class FilterForm(Form):
    __embassy_cities = UserDataDB.query.with_entities(UserDataDB.embassy).distinct().order_by('embassy asc')
    __interview_cities = UserDataDB.query.with_entities(UserDataDB.interview_location).distinct().order_by('interview_location asc')
    __streams = UserDataDB.query.with_entities(UserDataDB.stream).distinct().order_by('stream asc')

    embassy = SelectField('Embassy', choices=create_dict(__embassy_cities), coerce=str)
    stream = SelectField('Stream', choices=create_dict(__streams), coerce=str)
    interview_location = SelectField('Interview location', choices=create_dict(__interview_cities), coerce=str)
    chooser = SelectField('Dates to filter', choices=FILTER_CHOICES, coerce=str)
    from_date = StringField()
    to_date = StringField()

