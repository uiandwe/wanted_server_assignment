#!/usr/bin/env Python
# -*- coding: utf-8 -*-

from datetime import datetime

from app import db


class Company(db.Model):
    __tablename__ = 'company'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    created = db.Column(db.DateTime)

    def __init__(self):
        self.created = datetime.now()

    def __repr__(self):
        return 'id : %s' % (self.id)
