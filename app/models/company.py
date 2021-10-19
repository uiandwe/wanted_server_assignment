#!/usr/bin/env Python
# -*- coding: utf-8 -*-

from datetime import datetime

from app import db, app


class Company(db.Model):
    __tablename__ = 'company'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    created = db.Column(db.DateTime)

    def __init__(self):
        self.created = datetime.now()

    def __repr__(self):
        return 'id : %s' % (self.id)

    @staticmethod
    def create_company(params_data: dict, create_tags, create_company_info):
        try:
            company_name = params_data.get('company_name', {})
            tags = params_data.get('tags', {})

            company_instance = Company()
            dict_tag_language_instances = create_tags(tags)
            create_company_info(company_name, company_instance, dict_tag_language_instances)

            db.session.commit()
        except AssertionError as e:
            app.logger.error(e)
        except Exception as e:
            app.logger.error(e)
            db.session.rollback()
            raise Exception(str(e))
