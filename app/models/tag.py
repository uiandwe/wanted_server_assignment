#!/usr/bin/env Python
# -*- coding: utf-8 -*-

from app import db
from datetime import datetime


class Tag(db.Model):
    __tablename__ = 'tag'
    __table_args__ = {'mysql_collate': 'utf8_general_ci'}

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # company_id = db.Column(db.Integer, db.ForeignKey('company.id'))
    # company = db.relationship("company", backref="tag")

    # parent_id = Column(Integer, ForeignKey('parent.id'))

    name = db.Column(db.String(30))
    language = db.Column(db.String(10))
    created = db.Column(db.DateTime)

    def __init__(self, id, name, language, ):
        self.id = id
        self.name = name
        self.language = language
        self.created = datetime.now()

    def __repr__(self):
        return 'user_id : %s, user_name : %s, profile_url : %s' % (self.user_id, self.user_name, self.profile_url)

    def as_dict(self):
        return {x.name: getattr(self, x.name) for x in self.__table__.columns}
