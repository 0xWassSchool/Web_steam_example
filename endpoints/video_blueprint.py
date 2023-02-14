from endpoints._internal_core import *
from endpoints.utils.stream import *
from flask import Blueprint, request, render_template

stream = Blueprint("stream", __name__, url_prefix="/stream",
                  static_folder=static_path, template_folder=template_path + "stream/")
