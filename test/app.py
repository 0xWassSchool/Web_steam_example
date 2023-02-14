import hashlib

from core import DataRequest
from utils import Email, Database
from flask import Flask, render_template, make_response, request, abort


app = Flask(__name__, static_folder="static/", template_folder="templates/")
db = Database()
email = Email
data = DataRequest()


PEPER = "IIMvNCuuHSfTABDxygxWRmWQCqXuoYVMDJnbimhUETlOvroRyWuDIQCRXEXENNIgsnKGChOwYObSDTYPBLDIuhqUIWAqGkPZWiKHiyGOUAKJtBVPKCxSlAIMQvoSEmIXFYfQgHwGvNOsjHMABCMDBX"


def generate_secure_hash(ip: str, user_agent: str, language: str):
    seucre = ip + user_agent + language
    return PEPER + hashlib.sha384(seucre.encode()).hexdigest()


def secureDevice(func):
    def wrapper():
        if not generate_secure_hash(request.remote_addr, request.user_agent.string, "a") in db.getInfos(token=data.cookie["token"]):
            return abort(400)

        return func()
    return wrapper


@app.route("/r", methods=["POST"])
def register():
    get_json = request.get_json()

    account = db.createAccount(get_json["email"], get_json["username"], get_json["pwd"],
                               request.remote_addr, request.user_agent.string, "a")

    return {"token": account[0], "secure": account[1]}


@app.route("/login", methods=["POST"])
def login():
    getToDb = db.getInfos(email=data.json["email"], username=data.json["username"], password=hashlib.sha256(
        data.json["pwd"].encode()).hexdigest())


# da rifare ottimizzata la parte del login
app.run()
