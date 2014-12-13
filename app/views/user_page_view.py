__author__ = 'erik'

from flask import Blueprint, render_template, redirect, url_for, request
from flask_login import login_required, current_user
from app.utils.logger import Logger
from app.forms.user_edit_form import UserDataForm
from pycountry import countries

log = Logger()
logger = log.get_logger()
user_page = Blueprint('user', __name__)


@user_page.route('/user/<id>')
def show_user_page(id):
    from app.models.userdata import UserDataDB, UserDataView

    userdata = UserDataView(UserDataDB.query.get(id))
    return render_template('user_page.html', userdata=userdata)


@user_page.route('/user/edit', methods=['GET', 'POST'])
@login_required
def user_edit_page():
    from app.models.userdata import UserDataDB

    userdata = UserDataDB.query.filter_by(username=current_user.username).first()
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
        from app import db
        user_data = UserDataDB.query.filter_by(username=current_user.username)
        user_data.update(dict(
            from_full=countries.get(alpha2=form.from_full.data).name,
            from_short=form.from_full.data,
            stream=form.stream.data,
            interview_location=form.interview_location.data,
            interview_date=form.interview_date.data,
            invitation_to_apply_date=form.invitation_to_apply_date.data,
            mpnp_file_date=form.mpnp_file_date.data,
            mpnp_request_additional_docs_date=form.mpnp_request_additional_docs_date.data,
            mpnp_nomination_date=form.mpnp_nomination_date.data,
            cio_received_date=form.cio_received_date.data,
            cio_processing_fee_date=form.cio_processing_fee_date.data,
            cio_file_number=form.cio_file_number.data,
            embassy=form.embassy.data,
            ecas_recieved=form.ecas_recieved.data,
            ecas_in_process=form.ecas_in_process.data,
            ecas_additional_documents_request1=form.ecas_additional_documents_request1.data,
            ecas_medical_forms=form.ecas_medical_forms.data,
            ecas_medical_exam_passed=form.ecas_medical_exam_passed.data,
            ecas_medical_results_received=form.ecas_medical_results_received.data,
            ecas_additional_documents_request2=form.ecas_additional_documents_request2.data,
            povl_date=form.povl_date.data))
        db.session.commit()
        return redirect(url_for('user.show_user_page', id=user_data.first().id))
    return render_template('user_page_edit.html', userdata=userdata, form=form)

