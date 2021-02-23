#!/usr/bin/python3

from application import app
from flask import request, Response
import random

@app.route("/profile", methods=["GET", "POST"])
def profile():
    desc= {"Goalkeeper":["Gigantic", "Sweeper-Keeper"], "Defender":["Real-Leader", "No-Nonsense"], "Midfielder":["Keen eye for a pass", "Dribbling master"], "Striker":["Poacher", "Rapid"]}

    play=request.get_json()
    position1= play["position2"]
    nationality= char["nationality2"]
    a= ["Best in the world", "Mediocre, run-of-the-mill"]
    a.extend(desc[position1])
    a.extend(desc[nationality])
    b=random.choice(a)

    return Response(b, mimetype="text/plain")
