__author__ = 'erik'

from flask import render_template, request
from app import app
from app.models.userdata import UserDataDB, UserDataView
from app.forms.index_form import FilterForm

@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
    filter_form = FilterForm(csrf_enabled=False)
    if filter_form.validate():
        filter_dict = {}
        filter_state = ''
        if filter_form.embassy.data != '':
            filter_dict['embassy'] = filter_form.embassy.data
        if filter_form.interview_location.data != '':
            filter_dict['interview_location'] = filter_form.interview_location.data
        if filter_form.chooser.data != '':
            option = filter_form.chooser.data
            from_date = filter_form.from_date.data
            to_date = filter_form.to_date.data
            if option == 'mpnp_file_date':
                filter_state = UserDataDB.mpnp_file_date.between(from_date, to_date)
            elif option == 'cio_file_number':
                filter_state = UserDataDB.cio_file_number.between(from_date, to_date)
            elif option == 'ecas_medical_forms':
                filter_state = UserDataDB.ecas_medical_forms.between(from_date, to_date)
            elif option == 'povl_date':
                filter_state = UserDataDB.povl_date.between(from_date, to_date)


        user_data_objects = UserDataDB.query.filter(filter_state).filter_by(**filter_dict).order_by(UserDataDB.mpnp_file_date)
        users = [UserDataView(user) for user in user_data_objects]
        return render_template("index.html", user_data_objects=users, filter_form=filter_form)
    else:
        user_data_objects = UserDataDB.query.order_by(UserDataDB.mpnp_file_date)
        users = [UserDataView(user) for user in user_data_objects]
        return render_template("index.html", user_data_objects=users, filter_form=filter_form)



