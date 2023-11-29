from flask import Flask
from secrets import token_hex
from flask_wtf import CSRFProtect

def create_app() -> Flask:
    app: Flask = Flask(__name__)
    app.secret_key = token_hex(16)
    csrf: CSRFProtect = CSRFProtect(app)

    from contact_app.main.routes import main
    app.register_blueprint(main)

    return app
