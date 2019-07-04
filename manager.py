from bdc_wtss import app
from flask_script import Manager
import os


manager = Manager(app)


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