from flask import Flask, request, current_app
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

    return app
