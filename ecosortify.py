#!/usr/bin/python3
""" Defines flask application instance and tasks to manage app """
import os
from app import create_app

app = create_app(os.getenv('FLASK_CONFIG') or 'default')

if __name__ == '__main__':
    app.run(debug=True)