from flask import Flask, request, current_app
# configuration
from config import Config

from flask import Flask, request, current_app
# logging
import logging
from logging.handlers import SMTPHandler, RotatingFileHandler
# configuration
from config import Config

import os

def create_app(config_class=Config):
    # ini app
    app = Flask(__name__)
    # add config
    app.config.from_object(config_class)
    app.app_context().push()

    # the main of the app
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    # logs
    if not os.path.exists('logs'):
        os.mkdir('logs')
        file_handler = RotatingFileHandler('logs/oauth.log',
                                           maxBytes=10240, backupCount=10)
        file_handler.setFormatter(logging.Formatter(
            '%(asctime)s %(levelname)s: %(message)s '
            '[in %(pathname)s:%(lineno)d]'))
        file_handler.setLevel(logging.INFO)
        app.logger.addHandler(file_handler)
    app.logger.setLevel(logging.INFO)
    app.logger.info('Flask example startup')

    return app
