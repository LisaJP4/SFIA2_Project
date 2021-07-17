from application import db
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

class Fates(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    days = db.Column(db.String(200))
    fortunes = db.Column(db.String(200))
    outcomes = db.Column(db.String(200))