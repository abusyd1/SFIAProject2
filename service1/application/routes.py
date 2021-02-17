#!/usr/bin/python3 


from application import app, db
from application.models import Character
from flask import request, render_template, jsonify
import requests
import random
from sqlalchemy import desc

@app.route('/')
def index():
    class1 = requests.get("http://roller_service2:5000/position")
    play=Player.query.order_by(desc("Id")).limit(5).all()
    maxno=Player.query.order_by(desc("Id")).first()
    randno=random.randint(1,maxno.Id)
    randplay=Player.query.filter_by(Id=randno).all()
    new_player= Player(Player_position=position1.text)
    db.session.add(new_character)
    db.session.commit()
    
    return render_template("index.html", position=position1.text, play=play, randplay=randplay)

