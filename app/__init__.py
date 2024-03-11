#!/usr/bin/python3
""" Create application instance """
from flask import Flask
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from config import config

bootstrap = Bootstrap5()
db = SQLAlchemy()


def create_app(config_name):
    """ Creates an app """
    app = Flask(__name__)

    """ Configure application """
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    """ Initialize extensions """
    bootstrap.init_app(app)
    db.init_app(app)

    """ Register blueprints """
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    """ auth blueprint """
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)


    return app
