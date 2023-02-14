import json


# fernet key
key = b"xDuS4lLGaDghlVXHjxrPVp7COGeSXGEE4Ka9VUm-wHo="

# db config
databaseConfig = json.loads(open("./configs/database.json", "r").read())

# peper
PEPER = "IIMvNCuuHSfTABDxygxWRmWQCqXuoYVMDJnbimhUETlOvroRyWuDIQCRXEXENNIgsnKGChOwYObSDTYPBLDIuhqUIWAqGkPZWiKHiyGOUAKJtBVPKCxSlAIMQvoSEmIXFYfQgHwGvNOsjHMABCMDBX"

email_connection = [
    ("smtp.gmail.com", 587)
]

allowd_user_agent = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/109.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.78"
)
