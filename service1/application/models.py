#!/usr/bin/python3
from application import db
#from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired, NumberRange, Length

class Player(db.Model):
    Id=db.Column(db.Integer, primary_key=True)
    Player_position=db.Column(db.String(30), nullable=False)
    Player_nationality=db.Column(db.String(30), nullable=False)
    Player_profile= db.Column(db.String(3000), nullable=False)

    def __repr__(self):
        return f"{self.Id} | {self.Player_position} | {self.Player_nationlity}| {self.Player_profile}"
