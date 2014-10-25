__author__ = 'erik'

from flask import Blueprint, render_template



user_page = Blueprint('user', __name__)

@user_page.route('/user/<username>')
def show_user_page(username):
    from app.models.userdata import UserData
    userdata = UserData.objects(username=username).first()
    return render_template('user_page.html',userdata=userdata)