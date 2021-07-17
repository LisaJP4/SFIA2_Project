from application import db
from application.models import Fates
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db.drop_all()
db.create_all() 
db.session.commit()

trial = Fates(days="4", fortunes="Lucky")
db.session.add(trial)
db.session.commit()