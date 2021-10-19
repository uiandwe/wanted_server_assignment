#!/usr/bin/env Python
# -*- coding: utf-8 -*-

import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from app.config import config

app = Flask(__name__)

env = os.environ.get('env', 'dev')

# app config
app.config["SQLALCHEMY_DATABASE_URI"] = config[env].SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

from app.routes import *
from app.models import *

db.create_all()

from app.init_db import init_app

init_app(app)
