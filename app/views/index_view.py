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
        query = {}
        print('#'+filter_form.embassy.data+'#')
        if filter_form.embassy == '':
            query['embassy'] = {'$in': ['', None]}
        elif filter_form.embassy.data != '':
            query['embassy'] = filter_form.embassy.data
        user_data_objects = UserDataDB.objects(__raw__=query)
        users = [UserDataView(user) for user in user_data_objects]
        return render_template("index.html", user_data_objects=users, filter_form=filter_form)
    else:
        user_data_objects = UserDataDB.objects
        users = [UserDataView(user) for user in user_data_objects]
        return render_template("index.html", user_data_objects=users, filter_form=filter_form)



