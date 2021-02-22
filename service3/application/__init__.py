#!/usr/bin/python3

from flask import Flask
from os import getenv

app = Flask(__name__)
#app.config['SECRET_KEY'] = getenv('SECRET_KEY')
#app.config['SQLALCHEMY_DATABASE_URI'] = getenv('DATABASE_URI')


from application import routes
