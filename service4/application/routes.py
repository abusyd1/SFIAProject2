#!/usr/bin/python3

from application import app
from flask import request, Response
import random

@app.route("/profile", methods=["GET", "POST"])
def profile():
    info = request.data.decode('utf-8')
    data2 = info.split(".")
    position1 = data2[0]
    nationality1 = data2[1]
    print(position1)
    print(nationality1)
    keeper_profile = ['Towering', 'Sweeper']
    defender_profile = ['No-Nonsense', 'Commanding']
    midfielder_profile = ['Silky', 'All-Seeing']
    striker_profile = ['Prolific', 'Poacher']

    if position1 == "Goalkeeper":
        profile = random.choice(keeper_profile)
    if position1 == "Defender":
        profile = random.choice(defender_profile)
    if position1 == "Midfielder":
        profile = random.choice(midfielder_profile)
    if position1 == "Striker": 
        profile = random.choice(striker_profile)
    
    return Response(profile, mimetype="text/plain")