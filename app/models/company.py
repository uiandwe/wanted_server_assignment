#!/usr/bin/env Python
# -*- coding: utf-8 -*-

from datetime import datetime

from app import db


class Company(db.Model):
    __tablename__ = 'company'
    __table_args__ = (db.UniqueConstraint('name', 'language'),)

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(30))
    language = db.Column(db.String(10))
    created = db.Column(db.DateTime)

    tag = db.relationship("Tag", backref="company", secondary="company_tag")

    def __init__(self, name, language):
        self.name = name
        self.language = language
        self.created = datetime.now()

    def __repr__(self):
        return 'id : %s, name : %s, language : %s' % (self.id, self.name, self.language)

    def as_dict(self):
        d = {
            "company_name": self.name,
            "tags": [tag.name for tag in self.tag]
        }
        return d
