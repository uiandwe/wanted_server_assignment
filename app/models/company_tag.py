#!/usr/bin/env Python
# -*- coding: utf-8 -*-
from sqlalchemy.orm import relationship, backref
from app import db
from app.models.company import Company
from app.models.tag import Tag


class CompanyTag(db.Model):
    __tablename__ = 'company_tag'
    id = db.Column(db.Integer, primary_key=True)
    company_id = db.Column(db.Integer, db.ForeignKey('company.id'))
    tag_id = db.Column(db.Integer, db.ForeignKey('tag.id'))

    company = relationship(Company, backref=backref("company_tag", lazy='dynamic', cascade="all, delete-orphan"))
    tag = relationship(Tag, backref=backref("company_tag", lazy='dynamic', cascade="all, delete-orphan"))
