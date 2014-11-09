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
        if filter_form.embassy.data != '':
            filter_dict['embassy'] = filter_form.embassy.data
        user_data_objects = UserDataDB.query.filter_by(**filter_dict).order_by(UserDataDB.mpnp_file_date)
        users = [UserDataView(user) for user in user_data_objects]
        return render_template("index.html", user_data_objects=users, filter_form=filter_form)
    else:
        user_data_objects = UserDataDB.query.order_by(UserDataDB.mpnp_file_date)
        users = [UserDataView(user) for user in user_data_objects]
        return render_template("index.html", user_data_objects=users, filter_form=filter_form)



