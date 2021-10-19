#!/usr/bin/env Python
# -*- coding: utf-8 -*-

from collections import defaultdict
from datetime import datetime

from app import db
from app.models.language import Language
from app.models.util import get_or_create


class Tag(db.Model):
    __tablename__ = 'tag'
    __table_args__ = (db.UniqueConstraint('name', 'language_id'),)

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(30))
    created = db.Column(db.DateTime)

    language_id = db.Column(db.Integer, db.ForeignKey('language.id'))
    language = db.relationship("Language", backref="tag")

    def __init__(self, name, ):
        self.name = name
        self.created = datetime.now()

    def __repr__(self):
        return 'id : %s, name : %s' % (self.id, self.name)

    def as_dict(self):
        return {x.name: getattr(self, x.name) for x in self.__table__.columns}

    @staticmethod
    def create_tags(tags):

        dict_language_tags = defaultdict(list)
        for dict_tag_name in tags:
            for key in dict_tag_name['tag_name'].keys():
                name = dict_tag_name['tag_name'][key]
                language_dict = {'name': key}
                language_instance, _ = get_or_create(db.session, Language, **language_dict)

                tag_data = {'name': name}
                tag_instance, _ = get_or_create(db.session, Tag, **tag_data)
                tag_instance.language = language_instance
                dict_language_tags[key].append(tag_instance)

        return dict_language_tags
