#!/usr/bin/env Python
# -*- coding: utf-8 -*-

from datetime import datetime

from app import db


class Language(db.Model):
    __tablename__ = 'language'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(2))
    created = db.Column(db.DateTime)

    def __init__(self, name, ):
        self.name = name
        self.created = datetime.now()

    def __repr__(self):
        return 'id : %s, name : %s' % (self.id, self.name)
