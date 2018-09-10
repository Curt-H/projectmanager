from flask import Flask
from flasky.app.util import log
from flasky.app.main import main as main_route


def create_app():
    app = Flask(__name__)
    app.register_blueprint(main_route)
    return app


if __name__ == '__main__':
    app_test = create_app()
    config = dict(
        debug=True,
        host='localhost',
        port=80,
    )

    app_test.run(**config)
