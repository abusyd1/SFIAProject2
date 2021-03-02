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

    keeper_profile = ['-Towering-', '-Sweeper-Keeper-', '-Rapid Reflexes-']
    defender_profile = ['-Tactician-', '-Commanding-', '-Aerial Threat-']
    midfielder_profile = ['-Silky-', '-Eye for a Pass-', '-Engine-']
    striker_profile = ['-Prolific-', '-Poacher-', '-Speedster-']
    german_team = ['Bayern Munich', 'Borussia Dortmund', 'FC Schalke']
    french_team = ['PSG', 'AS Monaco', 'Marseille']
    english_team = ['Manchester United', 'Liverpool FC', 'Manchester City']
    portuguese_team = ['FC Porto', 'SL Benfica', 'Sporting CP']
    italian_team = ['Juventus FC', 'Napoli FC', 'Atalanta FC']
    spanish_team = ['FC Barcelona', 'Real Madrid', 'Atletico Madrid']
    american_team = ['LA Galaxy', 'New York City FC', 'Dallas FC']

    global profile
    if position1 == "Goalkeeper" and nationality1 == "English":
        profile = random.choice(keeper_profile) + " and plays for " + random.choice(english_team)
    if position1 == "Defender" and nationality1 == "English":
        profile = random.choice(defender_profile) + " and plays for " + random.choice(english_team)
    if position1 == "Midfielder" and nationality1 == "English":
        profile = random.choice(midfielder_profile) + " and plays for " + random.choice(english_team)
    if position1 == "Striker" and nationality1 == "English": 
        profile = random.choice(striker_profile) + " and plays for " + random.choice(english_team)

    if position1 == "Goalkeeper" and nationality1 == "Spanish":
        profile = random.choice(keeper_profile) + " and plays for " + random.choice(spanish_team)
    if position1 == "Defender" and nationality1 == "Spanish":
        profile = random.choice(defender_profile) + " and plays for " + random.choice(spanish_team)
    if position1 == "Midfielder" and nationality1 == "Spanish":
        profile = random.choice(midfielder_profile) + " and plays for " + random.choice(spanish_team)
    if position1 == "Striker" and nationality1 == "Spanish": 
        profile = random.choice(striker_profile) + " and plays for " + random.choice(spanish_team)
    
    if position1 == "Goalkeeper" and nationality1 == "French":
        profile = random.choice(keeper_profile) + " and plays for " + random.choice(french_team)
    if position1 == "Defender" and nationality1 == "French":
        profile = random.choice(defender_profile) + " and plays for " + random.choice(french_team)
    if position1 == "Midfielder" and nationality1 == "French":
        profile = random.choice(midfielder_profile) + " and plays for " + random.choice(french_team)
    if position1 == "Striker" and nationality1 == "French": 
        profile = random.choice(striker_profile) + " and plays for " + random.choice(french_team)
    
    if position1 == "Goalkeeper" and nationality1 == "Italian":
        profile = random.choice(keeper_profile) + " and plays for " + random.choice(italian_team)
    if position1 == "Defender" and nationality1 == "Italian":
        profile = random.choice(defender_profile) + " and plays for " + random.choice(italian_team)
    if position1 == "Midfielder" and nationality1 == "Italian":
        profile = random.choice(midfielder_profile) + " and plays for " + random.choice(italian_team)
    if position1 == "Striker" and nationality1 == "Italian": 
        profile = random.choice(striker_profile) + " and plays for " + random.choice(italian_team)
    
    if position1 == "Goalkeeper" and nationality1 == "German":
        profile = random.choice(keeper_profile) + " and plays for " + random.choice(german_team)
    if position1 == "Defender" and nationality1 == "German":
        profile = random.choice(defender_profile) + " and plays for " + random.choice(german_team)
    if position1 == "Midfielder" and nationality1 == "German":
        profile = random.choice(midfielder_profile) + " and plays for " + random.choice(german_team)
    if position1 == "Striker" and nationality1 == "German": 
        profile = random.choice(striker_profile) + " and plays for " + random.choice(german_team)
    
    if position1 == "Goalkeeper" and nationality1 == "American":
        profile = random.choice(keeper_profile) + " and plays for " + random.choice(american_team)
    if position1 == "Defender" and nationality1 == "American":
        profile = random.choice(defender_profile) + " and plays for " + random.choice(american_team)
    if position1 == "Midfielder" and nationality1 == "American":
        profile = random.choice(midfielder_profile) + " and plays for " + random.choice(american_team)
    if position1 == "Striker" and nationality1 == "American": 
        profile = random.choice(striker_profile) + " and plays for " + random.choice(american_team)
    
    if position1 == "Goalkeeper" and nationality1 == "Portuguese":
        profile = random.choice(keeper_profile) + " and plays for " + random.choice(portuguese_team)
    if position1 == "Defender" and nationality1 == "Portuguese":
        profile = random.choice(defender_profile) + " and plays for " + random.choice(portuguese_team)
    if position1 == "Midfielder" and nationality1 == "Portuguese":
        profile = random.choice(midfielder_profile) + " and plays for " + random.choice(portuguese_team)
    if position1 == "Striker" and nationality1 == "Portuguese": 
        profile = random.choice(striker_profile) + " and plays for " + random.choice(portuguese_team)
    return Response(profile, mimetype="text/plain")