__author__ = 'erik'
from app import dbm
from pycountry import countries
from datetime import datetime

COUNTRIES = [country.alpha2 for country in countries.objects]


class UserDataDB(dbm.Document):
    username = dbm.StringField(max_length=80, min_length=3, unique=True)
    stream = dbm.StringField()
    from_short = dbm.StringField()
    from_full = dbm.StringField()
    interview_location = dbm.StringField()
    interview_date = dbm.DateTimeField()
    invitation_to_apply_date = dbm.DateTimeField()
    mpnp_file_date = dbm.DateTimeField()
    mpnp_request_additional_docs_date = dbm.DateTimeField()
    mpnp_nomination_date = dbm.DateTimeField()
    cio_received_date = dbm.DateTimeField()
    cio_processing_fee_date = dbm.DateTimeField()
    cio_file_number = dbm.DateTimeField()
    embassy = dbm.StringField()
    ecas_recieved = dbm.DateTimeField()
    ecas_in_process = dbm.DateTimeField()
    ecas_additional_documents_request1 = dbm.DateTimeField()
    ecas_medical_forms = dbm.DateTimeField()
    ecas_medical_exam_passed = dbm.DateTimeField()
    ecas_medical_results_received = dbm.DateTimeField()
    ecas_additional_documents_request2 = dbm.DateTimeField()
    povl_date = dbm.DateTimeField()

    meta = {'collection': 'user_data'}


class UserDataView():
    def __init__(self, user_data_db, date_format='%d/%m/%Y'):
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