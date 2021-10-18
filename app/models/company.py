#!/usr/bin/env Python
# -*- coding: utf-8 -*-

from app import db
from datetime import datetime
from sqlalchemy.dialects.mysql import INTEGER


class Company(db.Model):
    __tablename__ = 'company'
    __table_args__ = {'mysql_collate': 'utf8_general_ci'}

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(30))
    language = db.Column(db.String(10))
    created = db.Column(db.DateTime)

    tag_id = db.Column(db.Integer, db.ForeignKey('tag.id'), nullable=True)
    tag = db.relationship("Tag", backref="company")

    def __init__(self, name, language):
        self.name = name
        self.language = language
        self.created = datetime.now()

    def __repr__(self):
        return 'id : %s, name : %s, language : %s' % (self.id, self.name, self.language)

    def as_dict(self):
        return {x.name: getattr(self, x.name) for x in self.__table__.columns}
