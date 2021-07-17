from flask import Flask, render_template, jsonify, Response
from flask_sqlalchemy import SQLAlchemy
import pymysql
import requests
import os
from os import getenv
from application import app, db
from application.models import Fates

# this must query the API for a number of days and a fortune to get an outcome based on these 
@app.route('/')
def home():
    days = requests.get('http://plague_days:5001/getday')
    fortune = requests.get('http://plague_fortune:5003/getfortune')
    outcome = requests.post('http://plague_outcome:5002/getoutcome', json={days.text : fortune.text})
    if fortune.text == "True":
        luck = "Lucky"
    else:
        luck = "Unlucky"
    latest = Fates(days=days.text, fortunes=fortune.text, outcomes=outcome.text)
    db.session.add(latest)
    db.session.commit()
    lastfivefates = Fates.query.order_by(Fates.id.desc()).limit(5).all()
    return render_template('plague.html', days=days.text, fortune=luck, outcome=outcome.text, lastfivefates=lastfivefates)
    