#!/usr/bin/env Python
# -*- coding: utf-8 -*-

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

# app config
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:1234qwer@0.0.0.0:3307/wanted"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


from app.routes import *
from app.models import *

db.create_all()
