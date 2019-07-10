"""Brazil Data Cube Web Time Series Series"""

import os
from flask import Flask
from flask_cors import CORS
from bdc_wtss.blueprint import blueprint
from bdc_wtss.config import get_settings


def create_app(config_name):
    """
    Creates Brazil Data Cube WTSS application from config object

    Args:
        config_name (string|bdc_wtss.config.Config) Config instance

    Returns:
        Flask Application with config instance scope

    """

    internal_app = Flask(__name__)

    with internal_app.app_context():
        internal_app.config.from_object(config_name)
        internal_app.register_blueprint(blueprint)

    return internal_app


app = create_app(
    get_settings(os.environ.get('ENVIRONMENT', 'DevelopmentConfig')))

CORS(app, resorces={r'/d/*': {"origins": '*'}})
