#!/usr/bin/env Python
# -*- coding: utf-8 -*-

from app import db
from datetime import datetime


class Tag(db.Model):
    __tablename__ = 'tag'
    __table_args__ = (db.UniqueConstraint('name', 'language'),)

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(30))
    language = db.Column(db.String(10))
    created = db.Column(db.DateTime)

    def __init__(self, name, language, ):
        self.name = name
        self.language = language
        self.created = datetime.now()

    def __repr__(self):
        return 'id : %s, name : %s, language : %s' % (self.id, self.name, self.language)

    def as_dict(self):
        return {x.name: getattr(self, x.name) for x in self.__table__.columns}
