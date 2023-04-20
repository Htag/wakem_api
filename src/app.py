import json
import os
import sys

from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager

from src.db.AlchemyEncoder import AlchemyEncoder
from src.exts import db, jwt
from src.views.account_view import account_view
from src.views.rider_view import rider_view
from src.views.driver_view import driver_view
from src.views.car_view import car_view

basedir = os.path.abspath(os.path.dirname(__file__))


def register_extensions(_app):
    db.init_app(_app)
    jwt.init_app(_app)


def register_views(_app):
    _app.register_blueprint(account_view)
    _app.register_blueprint(rider_view)
    _app.register_blueprint(driver_view)
    _app.register_blueprint(car_view)


def create_app(env) -> Flask:
    app = Flask(__name__)
    directory = basedir + os.sep + "config"
    if env == 'dev':
        app.debug = True
        print("Using Development configuration file...")
        app.config.from_file(os.path.join(directory, "dev.json"), load=json.load)
    elif env == 'local':
        app.debug = True
        print("Using Local configuration file...")
        app.config.from_file(os.path.join(directory, "local.json"), load=json.load)
    else:
        print("Using Production configuration file...")
        app.debug = False
        app.config.from_file(os.path.join(directory, "prod.json"), load=json.load)
    app.json_provider_class = AlchemyEncoder
    CORS(app, resources={r"/*": {"origins": "*"}})
    app.app_context().push()
    # app.json_encoder = CustomJSONEncoder
    register_extensions(app)
    register_views(app)
    return app


if __name__ == "__main__":
    # set debug to false when moving to production
    environment = sys.argv[1]
    print("creating app")
    wakem = create_app(environment)
    if environment == 'dev' or environment == 'local':
        wakem.run(host='0.0.0.0', port=5000)
    else:
        print("PROD")
