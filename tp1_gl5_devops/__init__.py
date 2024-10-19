import os

from flask import Flask


def createApp() -> Flask:
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.getrandom(25)
    app.config['API_PROXY'] = 'http://0.0.0.0:5000/'

    from .routes.api import api

    app.register_blueprint(api, url_prefix='/api/')

    return app
