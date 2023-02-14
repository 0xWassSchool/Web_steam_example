import ssl
import smtplib


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
            return 0
        except:
            return 1

        finally:
            self.server.quit()