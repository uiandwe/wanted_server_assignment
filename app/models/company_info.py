#!/usr/bin/env Python
# -*- coding: utf-8 -*-

from datetime import datetime

from app import db, app


class CompanyInfo(db.Model):
    __tablename__ = 'company_info'
    __table_args__ = (db.UniqueConstraint('name', 'language'),)

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(30))
    language = db.Column(db.String(10))
    created = db.Column(db.DateTime)

    company_id = db.Column(db.Integer, db.ForeignKey('company.id'))
    company = db.relationship("Company", backref="company_info")

    tag = db.relationship("Tag", backref="company_info", secondary="company_tag")

    def __init__(self, name, language):
        self.name = name
        self.language = language
        self.created = datetime.now()

    def __repr__(self):
        return 'id : %s, name : %s, language : %s, company: %s' % (self.id, self.name, self.language, self.company.id)

    def as_dict(self):
        d = {
            "company_name": self.name,
            "tags": [tag.name for tag in self.tag]
        }
        return d

    @staticmethod
    def company_info_find_query(**query):
        try:
            return CompanyInfo.query.filter_by(**query).first(), False
        except Exception as e:
            app.logger.error(e)
            return {"error": "company not found"}, True
