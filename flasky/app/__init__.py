from flask import Flask
from flasky.app.util import log


def create_app():
    app = Flask(__name__)

    return app


if __name__ == '__main__':
    app_test = create_app()
    config = dict(
        debug=True,
        host='0.0.0.0',
        port=80,
    )

    app_test.run(config)
