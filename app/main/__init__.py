#!/usr/bin/python3
""" Create main app blueprint """
from flask import Blueprint

main = Blueprint('main', __name__)

from . import views
