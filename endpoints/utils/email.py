import ssl
import smtplib

from utils.status_code import SUCCESS, GENERAL_ERROR


context = ssl.create_default_context()


class Email:
    def __init__(self, email, password, host, port) -> None:
        self.email = email
        self.password = password

        self.server = smtplib.SMTP(host, port)
        self.server.starttls(context=context)
        self.server.login(email, password)

    def sendEmail(self, reciver, subject, message):
        try:
            self.server.sendmail(self.email, reciver,
                                 f"Subject: {subject}\n\r\n\r{message}")
            return SUCCESS
        except:
            return GENERAL_ERROR

        finally:
            self.server.quit()