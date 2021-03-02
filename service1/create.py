#!/usr/bin/python3

from application import app, db
from application.models import Player

db.drop_all()
db.create_all()
