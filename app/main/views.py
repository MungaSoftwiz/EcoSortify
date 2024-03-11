#!/usr/bin/python3
""" """
from . import main


@main.route('/')
def index():
   return '<h1><b>This is a testing view</b></h1>'
