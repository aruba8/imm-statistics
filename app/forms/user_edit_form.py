__author__ = 'erik'

from flask_wtf import Form
from wtforms.fields import StringField, SelectField, DateField, TextField


class UserDataForm(Form):
    username = StringField()
    stream = SelectField(u'Stream')
    from_full = StringField()
    interview_location = StringField()
    interview_date = DateField()
    invitation_to_apply_date = DateField()
    mpnp_file_date = DateField()
    mpnp_request_additional_docs_date = DateField()
    mpnp_nomination_date = DateField()
    cio_received_date = DateField()
    cio_processing_fee_date = DateField()
    cio_file_number = DateField()
    embassy = StringField()
    ecas_recieved = DateField()
    ecas_in_process = DateField()
    ecas_additional_documents_request1 = DateField()
    ecas_medical_forms = DateField()
    ecas_medical_exam_passed = DateField()
    ecas_medical_results_received = DateField()
    ecas_additional_documents_request2 = DateField()
    povl_date = DateField()
