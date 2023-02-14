from endpoints._internal_core import *
from flask import Blueprint, request, render_template

ticket = Blueprint("ticket", __name__, url_prefix="/ticket",
                  static_folder=static_path, template_folder=template_path + "ticket/")
