import random

from endpoints._internal_core import *
from endpoints.utils.packet import securePacket, device
from endpoints.utils.status_code import EmailErrors, SUCCESS
from flask import Blueprint, request, session, make_response, render_template, redirect, abort

user = Blueprint("user", __name__, url_prefix="/me",
                 static_folder=static_path, template_folder=template_path + "user/")

emailError = EmailErrors()


def checkEmail(email):
    try:
        get_service = email.find("@")

        if not email[get_service:] in allowed_emails:
            return emailError.EMAIL_NOT_SUPPORTED
        else:
            return SUCCESS
    except:
        return emailError.INVALID_EMAIL


@user.route("/register")
@device
@securePacket
def register():
    return render_template("register.html")


@user.route("/checking")
@device
@securePacket
def checking_register():
    response = make_response
    email = request.form.get("email")
    username = request.form.get("username")
    password = request.form.get("password")

    check_email = checkEmail(email)

    if len(password) < 6:
        return {"status": "Password too small"}

    elif len(password) > 20:
        return {"status": "Password too long"}

    if not check_email == 0:
        # forced log
        print(check_email)
        return {"email": "error retry with another email"}

    createAccount = user_db.createAccount(email, username, password, request.remote_addr,
                                          request.user_agent.string, request.accept_languages)

    if isinstance(createAccount, int):
        return {"status": "username already taken"}

    response.set_cookie("token", createAccount[0])

    return response(render_template("checking_register.html", secure=createAccount[1]))
