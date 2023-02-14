import base64
import hashlib
import secrets
from pymongo import MongoClient


def generate_secure_hash(ip: str, user_agent: str, language: str, len: int):
    seucre = ip + user_agent + language
    return secrets.token_urlsafe(len) + hashlib.sha384(seucre.encode()).hexdigest()


class Database:
    client = MongoClient("mongodb://localhost:27017")
    db = client["test"]
    collection = db["test_1"]

    def createAccount(self, email: str,
                      username: str,
                      password: str,
                      ip: str,
                      agent: str,
                      language: str) -> tuple:
        token = secrets.token_urlsafe(40)
        secure = generate_secure_hash(ip, agent, language, len(username + password))

        self.collection.insert_one({
            "ip": base64.b64encode(ip.encode()).decode(),
            "email": email,
            "username": username,
            "password": hashlib.sha384(password.encode()).hexdigest(),
            "devices": [secure],
            "verifcation_client": []
        })
        return token, secure

    def updateElement(self, key, value, option, **kwargs):
        return self.collection.update_one({key: value}, {option : kwargs})

    def getInfos(self, **kwargs):
        return self.collection.find_one(kwargs, {"_id": 0})
