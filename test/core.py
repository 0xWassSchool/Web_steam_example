from flask import request


class DataRequest:
    try:
        json = request.get_json()
        cookie = request.cookies
    except:
        pass
