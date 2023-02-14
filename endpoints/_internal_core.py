from endpoints.utils import *

admin_db = AdminDatabase()
user_db = UserDatabse()


session_ = storeSession

# paths
static_path = r"static/"
template_path = r"templates/"


allowed_emails = (
    "gmail.com",
    "outlock.com",
    "yahoo.it",
)
