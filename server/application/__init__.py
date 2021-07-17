from flask import Flask, render_template, jsonify, Response
from flask_sqlalchemy import SQLAlchemy
import pymysql
import requests
import os
from os import getenv

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = getenv('DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 

db = SQLAlchemy(app)

SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY




    # for_outcome = {days.text : fortune.text}