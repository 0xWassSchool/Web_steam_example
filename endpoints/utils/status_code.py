SUCCESS = 0x1
GENERAL_ERROR = 0x0


class DatabaseErrors:
    # admin
    ACCOUNT_NOT_FOUND = 0x1

    # user
    ACCOUNT_ALREADY_EXIST = 0x2


class TicketErrors:
    TICKET_NOT_FOUND = 0x3


class EmailErrors:
    EMAIL_NOT_SUPPORTED = 0x4
    INVALID_EMAIL = 0x5


class PaymentErrors:
    ...

