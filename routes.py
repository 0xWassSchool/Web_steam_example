# not yet tested

from endpoints.utils.packet import securePacket
from flask import render_template, session, request, redirect, url_for

@securePacket
def index():
    return render_template("index.html")

@securePacket
def about():
    return render_template("about.html")

@securePacket
def contact():
    return render_template("contact.html")
