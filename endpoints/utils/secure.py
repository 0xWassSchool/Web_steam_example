import hashlib

from endpoints.utils._utils_core import PEPER

def generate_secure_hash(ip, user_agent, language):
    secure = ip + user_agent + language
    return PEPER + hashlib.sha384(secure.encode()).hexdigest()


def hashPassword(pwd: str):
    return hashlib.sha256(pwd.encode()).hexdigest()


def generate_serial(serial):
    return hashlib.sha512(serial).hexdigest()