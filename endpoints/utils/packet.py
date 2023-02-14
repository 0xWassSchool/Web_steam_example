from endpoints._internal_core import user_db
from endpoints.utils._utils_core import allowd_user_agent
from endpoints.utils.secure import generate_secure_hash

from flask import request, session, abort, redirect


def securePacket(func):
    """
    i use this function ( decorator ) for check if the user_agent is allowed and the session exist
    """
    def wrapper():
        if not request.user_agent.string in allowd_user_agent:
            return abort(400)

        if session.get("SESSION") is None:
            return redirect('/')

        return func()
    return wrapper


def device(func):
    """
    i use this function ( decorator ) for check if the device is into db
    """
    def wrapper():
        hash_ = generate_secure_hash(
            request.remote_addr, request.user_agent.string, str(request.accept_languages))
        if not hash_ in user_db.getInfos(token=request.cookies["token"]):
            return abort(400)

        return func()
    return wrapper

def auth(func):
    def wrapper():
        return func()

    return wrapper