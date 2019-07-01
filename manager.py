import os

from flask_cors import CORS
from flask_script import Manager

from bdc_wtss import create_app
from bdc_wtss.blueprint import blueprint
from bdc_wtss.config import get_settings


app = create_app(get_settings(os.environ.get('ENVIRONMENT', 'DevelopmentConfig')))
app.register_blueprint(blueprint)

manager = Manager(app)

CORS(app, resorces={r'/d/*': {"origins": '*'}})


@manager.command
def run():
    host = os.environ.get('SERVER_HOST', '0.0.0.0')
    try:
        port = int(os.environ.get('PORT', '5000'))
    except ValueError:
        port = 5000

    app.run(host, port)


if __name__ == '__main__':
    manager.run()