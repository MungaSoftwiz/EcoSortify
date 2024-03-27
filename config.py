#!/usr/bin/python3
""" Configuration for different environments during SDLC """
import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    """ Configures an app """
    SECRET_KEY = os.environ.get('SECRET_KEY')
    MAIL_SERVER = os.environ.get('MAIL_SERVER', 'smtp.mailgun.org')
    MAIL_PORT = os.environ.get('MAIL_PORT', '587')
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS', 'True')
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    ECOSORTIFY_MAIL_SUBJECT_PREFIX = '[Ecosortify]'
    ECOSORTIFY_MAIL_SENDER = 'Ecosortify Admin <ecosortify@placeholder.com'
    ECOSORTIFY_ADMIN = os.environ.get('ECOSORTIFY_ADMIN')

    @staticmethod
    def init_app(app):
        pass


class TestingConfiguration(Config):
    """ Testing environment config """
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
        'sqlite://'


class DevelopmentConfiguration(Config):
    """ Development environment config """
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')


config = {
    'testing': TestingConfiguration,
    'development': DevelopmentConfiguration,

    'default': DevelopmentConfiguration
}
