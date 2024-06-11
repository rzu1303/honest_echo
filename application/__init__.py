from flask import Flask
import logging
from flask_login import LoginManager

from config import Config

import logging
from logging.handlers import SMTPHandler, RotatingFileHandler
import os




login = LoginManager()

def create_app(config_class=Config):
    print('hey')
    app = Flask(__name__)
    app.config.from_object(config_class)
    

    from application.auth import bp as auth_bp
    # app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(auth_bp)

    from application.main import bp as main_bp
    app.register_blueprint(main_bp)

    from application.errors import bp as errors_bp
    app.register_blueprint(errors_bp)

    return app



from application import models

