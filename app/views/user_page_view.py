__author__ = 'erik'

from flask import Blueprint, render_template, redirect, url_for, request
from flask_login import login_required, current_user
from app.utils.logger import Logger
from app.forms.user_edit_form import UserDataForm
from pycountry import countries

log = Logger()
logger = log.get_logger()
user_page = Blueprint('user', __name__)


@user_page.route('/user/<username>')
def show_user_page(username):
    from app.models.userdata import UserDataDB, UserDataView

    userdata = UserDataView(UserDataDB.objects(username=username).first())
    return render_template('user_page.html', userdata=userdata)


@user_page.route('/user/edit', methods=['GET', 'POST'])
@login_required
def user_edit_page():
    from app.models.userdata import UserDataDB

    userdata = UserDataDB.objects(username=current_user.username).first()
    form = UserDataForm(username=userdata.username,
                        stream=userdata.stream,
                        interview_location=userdata.interview_location,
                        from_full=userdata.from_short,
                        interview_date=userdata.interview_date,
                        invitation_to_apply_date=userdata.invitation_to_apply_date,
                        mpnp_file_date=userdata.mpnp_file_date,
                        mpnp_request_additional_docs_date=userdata.mpnp_request_additional_docs_date,
                        mpnp_nomination_date=userdata.mpnp_nomination_date,
                        cio_received_date=userdata.cio_received_date,
                        cio_processing_fee_date=userdata.cio_processing_fee_date,
                        cio_file_number=userdata.cio_file_number,
                        embassy=userdata.embassy,
                        ecas_recieved=userdata.ecas_recieved,
                        ecas_in_process=userdata.ecas_in_process,
                        ecas_additional_documents_request1=userdata.ecas_additional_documents_request1,
                        ecas_medical_forms=userdata.ecas_medical_forms,
                        ecas_medical_exam_passed=userdata.ecas_medical_exam_passed,
                        ecas_medical_results_received=userdata.ecas_medical_results_received,
                        ecas_additional_documents_request2=userdata.ecas_additional_documents_request2,
                        povl_date=userdata.povl_date)

    if request.method == 'POST':
        UserDataDB.objects(username=current_user.username).update(
            set__from_full=countries.get(alpha2=form.from_full.data).name,
            set__from_short=form.from_full.data,
            set__stream=form.stream.data,
            set__interview_location=form.interview_location.data,
            set__interview_date=form.interview_date.data,
            set__invitation_to_apply_date=form.invitation_to_apply_date.data,
            set__mpnp_file_date=form.mpnp_file_date.data,
            set__mpnp_request_additional_docs_date=form.mpnp_request_additional_docs_date.data,
            set__mpnp_nomination_date=form.mpnp_nomination_date.data,
            set__cio_received_date=form.cio_received_date.data,
            set__cio_processing_fee_date=form.cio_processing_fee_date.data,
            set__cio_file_number=form.cio_file_number.data,
            set__embassy=form.embassy.data,
            set__ecas_recieved=form.ecas_recieved.data,
            set__ecas_in_process=form.ecas_in_process.data,
            set__ecas_additional_documents_request1=form.ecas_additional_documents_request1.data,
            set__ecas_medical_forms=form.ecas_medical_forms.data,
            set__ecas_medical_exam_passed=form.ecas_medical_exam_passed.data,
            set__ecas_medical_results_received=form.ecas_medical_results_received.data,
            set__ecas_additional_documents_request2=form.ecas_additional_documents_request2.data,
            set__povl_date=form.povl_date.data)
        return redirect(url_for('user.show_user_page', username=current_user.username))
    return render_template('user_page_edit.html', userdata=userdata, form=form)

