#!/usr/bin/python3

from application import app
from flask import request, Response
import random

@app.route("/nationality", methods=["GET"])
def nationality():
    nationalities = ["English", "French", "German", "Spanish", "Portuguese", "Italian", "American"]
    rannat= random.choice(nationalities)
    return Response(str(rannat), mimetype="text/plain")
