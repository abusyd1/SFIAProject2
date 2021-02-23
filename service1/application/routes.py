#!/usr/bin/python3 


from application import app, db
from application.models import Player
from flask import request, render_template, jsonify
import requests
import random
from sqlalchemy import desc

@app.route('/')
def index():
    position1 = requests.get("http://generator_service2:5001/position")
    nationality1 = requests.get("http://generator_service3:5002/nationality")
    profile = requests.get("http://generator_service4:5003/profile", json={"position2":position1.text, "nationality2":nationality1.text})
    play=Player.query.order_by(desc("Id")).limit(5).all()
    maxno=Player.query.order_by(desc("Id")).first()
    randno=random.randint(1,maxno.Id)
    randplay=Player.query.filter_by(Id=randno).all()
    new_player= Player(Player_position=position1.text, Player_nationality=nationality1.text, Player_profile=profile.text)
    db.session.add(new_player)
    db.session.commit()
    
    return render_template("index.html", position=position1.text,nationality=nationality1.text, profile=profile.text, play=play, randplay=randplay)

