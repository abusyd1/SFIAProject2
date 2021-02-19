#!/usr/bin/python3

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

SECRET_KEY = os.urandom(32)

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:root@34.83.244.57/Project22"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = SECRET_KEY
db = SQLAlchemy(app)

from application import routes
