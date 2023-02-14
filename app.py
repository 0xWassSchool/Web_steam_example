from routes import *
from endpoints.core import *
from flask import Flask

app = Flask(__name__, template_folder="templates", static_folder="static")
app.secret_key = "my-secret-key"

# blueprints
app.register_blueprint(admin)
app.register_blueprint(user)
app.register_blueprint(ticket)
app.register_blueprint(stream)

# static endpoints
app.add_url_rule('/', "index", index)
app.add_url_rule("/about", "about", about)
app.add_url_rule("/contact", "contact", contact)
