#!/usr/bin/python3 


from application import app, db
from application.models import Player
from flask import request, render_template
import requests
import random
from sqlalchemy import desc

@app.route('/', methods = ['GET', 'POST'])
def index():
    position1 = requests.get("http://generator_service2:5001/position")
    string_position1 = position1.text
    nationality1 = requests.get("http://generator_service3:5002/nationality")
    string_nationality1 = nationality1.text
    info = str(position1.text) + "." + str(nationality1.text)
    profile = requests.post("http://generator_service4:5003/profile", data = info)

  
   # new_player= Player(Player_position=position1.text, Player_nationality=nationality1.text, Player_profile=profile.text)
   # db.session.add(new_player)
   # db.session.commit()
    
    return render_template("index.html", position1=string_position1,nationality1=string_nationality1, info=info, profile=profile.text)

