__author__ = 'erik'
from app import dbm

COUNTRIES = ('RU', 'UA', 'BY', 'KZ', 'MD', 'IL', 'LV', 'UZ', 'CA', 'US', 'AM', 'KG')


class UserData(dbm.Document):
    username = dbm.StringField(max_length=80, min_length=3, unique=True)
    stream = dbm.StringField(choices=('general', 'strategic', 'family'))
    from_short = dbm.StringField(choices=COUNTRIES)
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
