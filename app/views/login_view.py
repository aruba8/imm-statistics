__author__ = 'erik'

from flask import render_template, flash, redirect, request, url_for, g
from flask_login import login_user, logout_user, login_required
from pycountry import countries
from app.forms.login_form import LoginForm
from app.forms.signup_form import SignUpForm
from app.models.user import User
from app.sessions import Sessions
from app import lm

sessions = Sessions()

from app import app

@lm.user_loader
def user_loader(login):
    return User.objects(username=login).first()


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if g.user.is_authenticated():
        return redirect(url_for('index'))

    if form.validate_on_submit():
        username = form.login.data
        user = User.objects(username=username).first()
        if sessions.validate_login(username, form.password.data, {}):
            sessions.start_session(username)
            login_user(user)
            flash("Logged in successfully.")
            return redirect(request.args.get('next') or url_for('user.show_user_page', username=username))
    return render_template('login.html', form=form)

@app.route('/signup', methods=['GET', 'POST'])
def signup_page():
    form = SignUpForm()
    if request.method == 'GET':
        return render_template('signup.html', form=form)
    if request.method == 'POST' and form.validate() and sessions.validate_new_user(form.login.data, form.password.data,
                                                                                   form.confirm.data):
        if sessions.new_user(form.login.data, form.password.data):
            user = User.objects(username=form.login.data).first()
            print user.username
            login_user(user)
            from app.models.userdata import UserDataDB
            # UserDataDB(username=user.username, from_full=countries.get(alpha2=form.country.data).name).save()
            return redirect(url_for('user.show_user_page', username=user.username))
        else:
            return redirect(url_for('signup_page'))
    else:
        return redirect(url_for('signup_page'))

@app.route('/logout')
@login_required
def logout():
    # Remove the user information from the session
    logout_user()
    return redirect(request.args.get('next') or '/index')

