#!/usr/bin/python3

from application import app
from flask import request, Response
import random

@app.route("/position", methods=["GET"])
def position():
    positions = ["Goalkeeper", "Defender", "Midfielder", "Striker"]
    rposition= random.choice(positions)
    return Response(str(rposition), mimetype="text/plain")
