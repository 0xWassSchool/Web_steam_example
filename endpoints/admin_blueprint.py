from endpoints._internal_core import *
from endpoints.utils.packet import securePacket
from flask import Blueprint, request, session, render_template, abort, redirect


admin = Blueprint("admin", __name__, url_prefix="/admin",
                  static_folder=static_path, template_folder=template_path + "admin/")


@admin.route("/login")
@securePacket
def loginAdmin():
    return render_template("login.html")


@admin.route("/check", methods=["POST"])
@securePacket
def checkCredentials():

    username = request.form.get("username")
    password = request.form.get("pwd")

    getToken = admin_db.checkCredenzials(username, password)
    print(password)

    if getToken == 1:
        return {"status": "incorrect username or password"}

    return render_template("check.html", token=getToken)


@admin.route("/page")
@securePacket
def page():
    # code ...
    return render_template("page.html")


@admin.route("/event/add", methods=["POST"])
@securePacket
def addEvent():
    # code ...
    return render_template("event.html.html")


@admin.route("/event/modify", methods=["PATCH"])
@securePacket
def modifyEvent():
    # code ...
    return render_template("modifying_html.html")


@admin.route("/event/delete", methods=["DELETE"])
@securePacket
def deleteEvent():
    # code ...
    return render_template("deleting_event.html")
