from app.models.email import EmailConfirmation
from app.models.user import User
from app.sessions import Sessions

__author__ = 'erik'
from app import app
from flask import redirect, request, render_template
from datetime import datetime


session = Sessions()


@app.route("/confirm")
def confirm():
    if request.args.get("user_id") and request.args.get("hash"):
        user_id = request.args.get("user_id")
        hash_c = request.args.get("hash")
        user = User.query.filter_by(id=user_id).first()
        if user.email_activated:
            message = "You email has already activated!"
            return render_template("confirm.html", message=message)

        if validate(user_id, hash_c):
            message = "Your email confirmed!"
            user.email_activated = True
            session.save(user)
            return render_template("confirm.html", message=message)
        else:
            message = "Your confirmation link expired or wrong!"
            return render_template("confirm.html", message=message)
    return redirect("index")


def validate(user_id, hash_c):
    current_time = datetime.now()
    email_conf = EmailConfirmation.query.filter_by(user_id=user_id).first()
    if email_conf.hash_c == hash_c and email_conf.expiration_date > current_time:
        email_conf.activation_time = current_time
        session.save(email_conf)
        return True
    else:
        return False

