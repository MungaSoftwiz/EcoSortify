#!/usr/bin/python3
""" Defines flask application instance and tasks to manage app """
import os
from app import create_app, db
from flask_migrate import Migrate

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
database_migrate = Migrate(app, db, include_schema=True)


@app.shell_context_processor
def create_shell_context():
    """ Automate importing of the database instance and models
    when a flask shell session starts
    """
    return dict(db=db, User=User, Post=Post, Comment=Comment)
