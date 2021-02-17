#!/usr/bin/python3

from application import app
from flask import request, Response
import random

@app.route("/position", methods=["GET"])
def position():
    positions = ["Goalkeeper", "Right-Back", "Centreback", "Left-Back", "Centre Defensive Midfielder", "Centre Attacking Midfielder", "Left Winger", "Right Winger"]
    rposition= random.choice(positions)
    return Response(str(rposition), mimetype="text/plain")
