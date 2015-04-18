from uuid import uuid4

from flask import render_template, flash, redirect, request, url_for, g, current_app, session, abort
from flask_login import login_user, logout_user, login_required
from pycountry import countries
from flask_principal import Identity, identity_changed, AnonymousIdentity
from datetime import datetime, timedelta

from app.forms.forgot_form import Forgot
from app.forms.reset_password_form import ResetPassword
from app.models.reset import Reset
from app.models.userdata import UserDataDB
from app.forms.login_form import LoginForm
from app.forms.signup_form import SignUpForm
from app.models.user import User
from app.sessions import Sessions
from app import lm
from app.utils.mailer import send_password_recovery_email


sessions = Sessions()

from app import app, db


@lm.user_loader
def user_loader(username):
    return User.query.filter_by(username=username).first()


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if g.user.is_authenticated():
        return redirect(url_for('index'))

    if form.validate_on_submit():
        username = form.login.data
        user = User.query.filter_by(username=username).first()
        if sessions.validate_login(username, form.password.data):
            sessions.start_session(username)
            login_user(user)
            userdata = UserDataDB.query.filter_by(username=user.username).first()
            flash("Logged in successfully.")
            # Tell Flask-Principal the identity changed
            identity_changed.send(current_app._get_current_object(), identity=Identity(user.id))
            return redirect(request.args.get('next') or url_for('user.show_user_page', _id=userdata.id))

    return render_template('login.jinja2.html', form=form)


@app.route('/signup', methods=['GET', 'POST'])
def signup_page():
    form = SignUpForm()
    if request.method == 'GET':
        return render_template('signup.jinja2.html', form=form)
    if request.method == 'POST' and form.validate() and validate_new_user(form.login.data, form.password.data,
                                                                                   form.confirm.data):
        user_data = UserDataDB.query.filter_by(username=form.login.data)
        if len(user_data.all()) == 0:
            if sessions.new_user(form.login.data, form.email.data, form.password.data):
                user_data = UserDataDB(username=form.login.data, from_full=countries.get(alpha2=form.country.data).name,
                                       from_short=form.country.data)
                db.session.add(user_data)
                db.session.commit()
                user = User.query.filter_by(username=form.login.data).first()
                login_user(user)
                return redirect(url_for('user.show_user_page', _id=user.id))
        else:
            sessions.new_user(form.login.data, form.email.data, form.password.data, _id=user_data.first().id)
            user = User.query.filter_by(username=form.login.data).first()
            login_user(user)
            return redirect(url_for('user.show_user_page', _id=user.id))
    else:
        return render_template('signup.jinja2.html', form=form)


@app.route('/logout')
@login_required
def logout():
    # Remove the user information from the session
    logout_user()
    # Remove session keys set by Flask-Principal
    for key in ('identity.name', 'identity.auth_type'):
        session.pop(key, None)

    # Tell Flask-Principal the user is anonymous
    identity_changed.send(current_app._get_current_object(), identity=AnonymousIdentity())

    return redirect(request.args.get('next') or '/index')


@app.route('/forgot', methods=['GET', 'POST'])
def forgot():
    form = Forgot()
    if form.validate_on_submit():
        email = form.email.data
        user = User.query.filter_by(email=email).first()
        reset_obj = Reset.query.filter_by(user_id=user.id).first()
        if user and not user.email_activated:
            return render_template("forgot_sent.jinja2.html",
                                   message='We cannot reset your password because your email was not confirmed')

        if user and not reset_obj and user.email_activated:
            expiration_date = datetime.now() + timedelta(days=1)
            reset_obj = Reset(user_id=user.id, uuid=uuid4(), expiration_date=expiration_date)
            db.session.add(reset_obj)
            db.session.commit()
        elif user and reset_obj and user.email_activated:
            reset_obj.uuid = uuid4()
            reset_obj.expiration_date = datetime.now() + timedelta(days=1)
            db.session.add(reset_obj)
            db.session.commit()
        send_password_recovery_email(reset_obj, user)
        return render_template("forgot_sent.jinja2.html", message='Recover link sent on your email')

    return render_template('forgot.jinja2.html', form=form)


@app.route("/reset/<uuid>", methods=["GET", "POST"])
def reset(uuid):
    reset_obj = Reset.query.filter_by(uuid=uuid).first()
    reset_form = ResetPassword()
    if reset_form.validate_on_submit():
        password = reset_form.password.data
        user = User.query.filter_by(id=reset_obj.user_id).first()
        sessions.update_password(password, user)
        sessions.delete_row(reset_obj)
        return redirect(url_for('login'))

    if reset_obj and reset_obj.expiration_date > datetime.now():
        return render_template('reset_password.html', form=reset_form, reset=reset_obj)
    elif reset_obj and reset_obj.expiration_date < datetime.now():
        return render_template('forgot_sent.jinja2.html',
                               message='We cannot reset your password because link has expired')
    abort(404)
