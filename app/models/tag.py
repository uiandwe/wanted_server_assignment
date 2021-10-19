#!/usr/bin/env Python
# -*- coding: utf-8 -*-

from datetime import datetime
from collections import defaultdict
from app import db
from app.models.util import get_or_create


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

    @staticmethod
    def create_tags(tags):

        dict_language_tags = defaultdict(list)
        for dict_tag_name in tags:
            for key in dict_tag_name['tag_name'].keys():
                name = dict_tag_name['tag_name'][key]
                language = key

                d = {'name': name, 'language': language}
                instance, _ = get_or_create(db.session, Tag, **d)
                dict_language_tags[key].append(instance)

        return dict_language_tags
