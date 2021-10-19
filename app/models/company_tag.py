#!/usr/bin/env Python
# -*- coding: utf-8 -*-
from sqlalchemy.orm import relationship, backref

from app import db
from app.models.company_info import CompanyInfo
from app.models.tag import Tag


class CompanyTag(db.Model):
    __tablename__ = 'company_tag'
    id = db.Column(db.Integer, primary_key=True)
    company_info_id = db.Column(db.Integer, db.ForeignKey('company_info.id'))
    tag_id = db.Column(db.Integer, db.ForeignKey('tag.id'))

    company_info = relationship(CompanyInfo,
                                backref=backref("company_tag", lazy='dynamic', cascade="all, delete-orphan"))
    tag = relationship(Tag, backref=backref("company_tag", lazy='dynamic', cascade="all, delete-orphan"))
