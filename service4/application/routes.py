#!/usr/bin/python3

from application import app
from flask import request, Response
import random

@app.route("/profile", methods=["GET", "POST"])
def profile():
    desc= {"Goalkeeper":["Gigantic", "Sweeper-Keeper"], "Defender":["Real-Leader", "No-Nonsense"], "Midfielder":["Keen eye for a pass", "Dribbling master"], "Striker":["Poacher", "Rapid"]}

    play=request.get_json()
    position1= play["class2"]
    race= char["race2"]
    a= ["Completely useless", "Super evil"]
    a.extend(desc[class1])
    a.extend(desc[race])
    b=random.choice(a)

    return Response(b, mimetype="text/plain")
