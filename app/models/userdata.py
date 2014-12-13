__author__ = 'erik'
from app import db
from pycountry import countries
from datetime import datetime

COUNTRIES = [country.alpha2 for country in countries.objects]


class UserDataDB(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = (db.Integer)
    username = db.Column(db.String(length=80), db.ForeignKey('user.username'))
    stream = db.Column(db.String(collation='NOCASE'))
    from_short =db.Column(db.String())
    from_full = db.Column(db.String())
    interview_location = db.Column(db.String(collation='NOCASE'))
    interview_date = db.Column(db.DateTime())
    invitation_to_apply_date = db.Column(db.DateTime())
    mpnp_file_date = db.Column(db.DateTime())
    mpnp_request_additional_docs_date = db.Column(db.DateTime())
    mpnp_nomination_date = db.Column(db.DateTime())
    cio_received_date = db.Column(db.DateTime())
    cio_processing_fee_date = db.Column(db.DateTime())
    cio_file_number = db.Column(db.DateTime())
    embassy = db.Column(db.String(collation='NOCASE'))
    ecas_recieved = db.Column(db.DateTime())
    ecas_in_process = db.Column(db.DateTime())
    ecas_additional_documents_request1 = db.Column(db.DateTime())
    ecas_medical_forms = db.Column(db.DateTime())
    ecas_medical_exam_passed = db.Column(db.DateTime())
    ecas_medical_results_received = db.Column(db.DateTime())
    ecas_additional_documents_request2 = db.Column(db.DateTime())
    povl_date = db.Column(db.DateTime())

    def __repr__(self):
        return '<UserDataDB %r>' % self.username



class UserDataView():
    def __init__(self, user_data_db, date_format='%d/%m/%Y'):
        self.user_id = self.__set_field(user_data_db.id)
        self.date_format = date_format
        self.username = self.__set_field(user_data_db.username)
        self.stream = self.__set_field(user_data_db.stream)
        self.from_short = self.__set_field(user_data_db.from_short)
        self.from_full = self.__set_field(user_data_db.from_full)
        self.interview_location = self.__set_field(user_data_db.interview_location)
        self.interview_date = self.__set_field(user_data_db.interview_date)
        self.invitation_to_apply_date = self.__set_field(user_data_db.invitation_to_apply_date)
        self.mpnp_file_date = self.__set_field(user_data_db.mpnp_file_date)
        self.mpnp_request_additional_docs_date = self.__set_field(user_data_db.mpnp_request_additional_docs_date)
        self.mpnp_nomination_date = self.__set_field(user_data_db.mpnp_nomination_date)
        self.cio_received_date = self.__set_field(user_data_db.cio_received_date)
        self.cio_processing_fee_date = self.__set_field(user_data_db.cio_processing_fee_date)
        self.cio_file_number = self.__set_field(user_data_db.cio_file_number)
        self.embassy = self.__set_field(user_data_db.embassy)
        self.ecas_recieved = self.__set_field(user_data_db.ecas_recieved)
        self.ecas_in_process = self.__set_field(user_data_db.ecas_in_process)
        self.ecas_additional_documents_request1 = self.__set_field(user_data_db.ecas_additional_documents_request1)
        self.ecas_medical_forms = self.__set_field(user_data_db.ecas_medical_forms)
        self.ecas_medical_exam_passed = self.__set_field(user_data_db.ecas_medical_exam_passed)
        self.ecas_medical_results_received = self.__set_field(user_data_db.ecas_medical_results_received)
        self.ecas_additional_documents_request2 = self.__set_field(user_data_db.ecas_additional_documents_request2)
        self.povl_date = self.__set_field(user_data_db.povl_date)

    def __set_field(self, field):
        if field is None or field == '':
            return ''
        elif isinstance(field, datetime):
            return field.strftime(self.date_format)
        else:
            return field