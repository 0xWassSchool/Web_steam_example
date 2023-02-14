# -*- codeing: utf-8 -*-

import time
import base64
import secrets

from pymongo import MongoClient
import endpoints.utils.secure as secure
import endpoints.utils.status_code as status_code
from endpoints.utils._utils_core import databaseConfig


dbErrors = status_code.DatabaseErrors()
ticketErrors = status_code.TicketErrors()

client = MongoClient(databaseConfig["host"])
database = client[databaseConfig["db"]]


def storeSession(ip: str, user_agent: str):
    session = base64.b64encode(
        ip.encode() + b'@' + user_agent.encode()).decode()

    collection = database[databaseConfig["collections"][4]]

    collection.insert_one({"session": session})

    return session


class AdminDatabase:
    collection = database[databaseConfig["collections"][0]]

    def checkCredenzials(self, username, password) -> int | str:
        get_token = self.collection.find_one(
            {"username": username, "password": secure.hashPassword(password)})

        if get_token:
            return get_token["token"]

        return dbErrors.ACCOUNT_NOT_FOUND


class UserDatabse:
    collection = database[databaseConfig["collections"][1]]

    def _checkAccountAlreadyExist(self, username):
        if self.collection.find_one({"username": username}):
            return dbErrors.ACCOUNT_ALREADY_EXIST

    def createAccount(self, email: str,
                      username: str,
                      pwd: str,
                      ip: str,
                      user_agent: str,
                      language: str) -> int | str:
        if check := self._checkAccountAlreadyExist(username) == 2:
            return check

        # prendere spunto da /test/app.py

    def getUserInfo(self, **kwargs):
        return self.collection.find_one(kwargs, {"_id": 0})

    def updateUser(self, token, option, **kwargs):
        return self.collection.update_one({"token": token}, {option: kwargs})


class TicketDatabase:
    collection = database[databaseConfig["collections"][2]]

    def createTickets(self, name, artist, number) -> int:
        info = base64.b85encode(f"{name}&{artist}".encode()).decode()

        for num in range(number + 1):
            serial = secrets.token_urlsafe(90)
            timestamp = str(int(time.time()) + num)

            ticket = str(hex(num)) + "." + serial + \
                "." + timestamp + "." + info

            self.collection.insert_one({
                "ticket": ticket,
                "ticket_number": num,
                "serial": serial,
                "info": info,
                "time": timestamp,
                "account": ""
            })

        return status_code.SUCCESS

    def assignTicket(self, token, ticket) -> int:
        try:
            self.collection.update_one(
                {"ticket": ticket}, {"$set": {"account": token}})
            return status_code.SUCCESS
        except:
            return status_code.GENERAL_ERROR

    def validateTicket(self, ticket) -> int:
        get_ticket = self.collection.find_one({"ticket": ticket})

        if get_ticket is None:
            return ticketErrors.TICKET_NOT_FOUND

        ticket_part = ticket.split(".")

        check = all((
            ticket_part[0] == get_ticket["ticket_number"],
            ticket_part[1] == get_ticket["serial"],
            ticket_part[2] == get_ticket["time"],
            ticket_part[3] == get_ticket["info"],
        ))

        result = status_code.SUCCESS if check is True else None

        return result


class EventDatabase:
    collection = database[databaseConfig["collections"][3]]

    def AddEvent(self, name,
                 date,
                 artist,
                 max_tickets: int) -> int:

        self.collection.insert_one({
            "name": name,
            "date": date,
            "artist": artist,
            "max_tickets": max_tickets
        })

        return status_code.SUCCESS

    def modifyEvent(self, name, key, new_element) -> int:
        return self.collection.update_one({"name": name}, {"$set": {key: new_element}})

    def deleteEvent(self, name) -> int:
        return self.collection.delete_one({"name": name})
