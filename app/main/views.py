#!/usr/bin/python3
""" Contains routes """
from . import main


@main.route('/')
def index():
    """ Tests view for the app """
    return '<h1><b>This is a testing view</b></h1>'
