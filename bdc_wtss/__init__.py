from bdc_wtss.blueprint import blueprint
from bdc_wtss.config import get_settings
from flask import Flask
from flask_cors import CORS
import os


def create_app(config_name):
    app = Flask(__name__)

    with app.app_context():
        app.config.from_object(config_name)
        app.register_blueprint(blueprint)

    return app


app = create_app(get_settings(os.environ.get('ENVIRONMENT', 'DevelopmentConfig')))

CORS(app, resorces={r'/d/*': {"origins": '*'}})