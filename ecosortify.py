#!/usr/bin/python3
""" Defines flask application instance and tasks to manage app """
import os
from app import create_app

app = create_app(os.getenv('FLASK_CONFIG') or 'default')


@app.shell_context_processor
def create_shell_context():
    """ Automate importing of the database instance and models
    when a flask shell session starts
    """
    return dict(db=db, User=User, Post=Post, Comment=Comment)
