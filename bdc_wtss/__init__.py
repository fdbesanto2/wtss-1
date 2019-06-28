from flask import Flask


def create_app(config_name):
    app = Flask(__name__)

    with app.app_context():
        app.config.from_object(config_name)

    return app