__author__ = 'erik'

from flask_wtf import Form
from wtforms.fields import StringField, SelectField, DateField
from pycountry import countries

from app.utils.helper import INTERVIEW_CITIES, EMBASSY_CITIES


COUNTRIES = [country.alpha2 for country in countries.objects]
STREAM_CHOICES = [('general', 'general'), ('family', 'family'), ('strategic', 'strategic')]


def create_countries_dict():
    country_dict = []
    for country_ in COUNTRIES:
        country_dict.append((country_, countries.get(alpha2=country_).name))
    return country_dict


def create_dict(source):
    return [(city, city) for city in source]

date_format = '%d/%m/%Y'

class UserDataForm(Form):
    username = StringField()
    stream = SelectField(u'Stream', choices=STREAM_CHOICES)
    from_full = SelectField(choices=create_countries_dict())
    interview_location = SelectField(choices=create_dict(INTERVIEW_CITIES))
    interview_date = DateField(format=date_format)
    invitation_to_apply_date = DateField(format=date_format)
    mpnp_file_date = DateField(format=date_format)
    mpnp_request_additional_docs_date = DateField(format=date_format)
    mpnp_nomination_date = DateField(format=date_format)
    cio_received_date = DateField(format=date_format)
    cio_processing_fee_date = DateField(format=date_format)
    cio_file_number = DateField(format=date_format)
    embassy = SelectField(choices=create_dict(EMBASSY_CITIES))
    ecas_recieved = DateField(format=date_format)
    ecas_in_process = DateField(format=date_format)
    ecas_additional_documents_request1 = DateField(format=date_format)
    ecas_medical_forms = DateField(format=date_format)
    ecas_medical_exam_passed = DateField(format=date_format)
    ecas_medical_results_received = DateField(format=date_format)
    ecas_additional_documents_request2 = DateField(format=date_format)
    povl_date = DateField(format=date_format)


