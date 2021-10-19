#!/usr/bin/env Python
# -*- coding: utf-8 -*-

from collections import defaultdict

from flask import jsonify, request

from app import app, db
from app.models.company import Company
from app.models.company_info import CompanyInfo
from app.models.tag import Tag
from app.models.util import get_or_create
from app.validtors.company import CompanyPostSchema, CompanyGetSchema
from sqlalchemy.orm.exc import NoResultFound


@app.route('/companies/<companyName>', methods=['get'])
def get_company(companyName):
    # TODO 데코레이터로 안되나?
    wanted_language = request.headers.get('x-wanted-language', '')

    try:
        valid_data = {"company_name": companyName, "wanted_language": wanted_language}
        error = CompanyGetSchema().validate(data=valid_data)
        if error:
            raise ValueError(error)

        company_info = CompanyInfo.query.filter_by(name=companyName).one()
        query = {
            "company": company_info.company,
            "language": wanted_language
        }

        instance, error = CompanyInfo.company_info_find_query(**query)
        if error:
            raise AttributeError("company not found")

    except NoResultFound as e:
        return jsonify({"error": "company not found"}), 404
    except Exception as e:
        app.logger.error(e)
        return jsonify({"error": str(e)}), 404

    return jsonify(instance.as_dict())


@app.route('/companies', methods=['post'])
def create_company():
    wanted_language = request.headers.get('x-wanted-language', 'ko')

    params_json = request.get_json()
    params_json['wanted_language'] = wanted_language

    try:
        error = CompanyPostSchema().validate(data=params_json)
        if error:
            raise ValueError(error)

    except ValueError as e:
        return jsonify({"error": e}), 400

    try:
        company = Company()

        tags = params_json.get('tags', {})

        tag_name = defaultdict(list)
        for dict_tag_name in tags:
            for key in dict_tag_name['tag_name'].keys():
                name = dict_tag_name['tag_name'][key]
                language = key

                d = {'name': name, 'language': language}
                instance, _ = get_or_create(db.session, Tag, **d)
                tag_name[key].append(instance)

        company_name = params_json.get('company_name', {})
        for language in company_name:
            d = {
                "language": language,
                "name": company_name[language]
            }

            instance, instance_exist = get_or_create(db.session, CompanyInfo, **d)
            if not instance_exist:
                raise IOError("company existed")

            instance.company = company
            for t in tag_name[language]:
                instance.tag.append(t)
            db.session.add(instance)

        db.session.commit()
    except IOError as e:
        app.logger.error(e)
        # db.session.rollback()

    except Exception as e:
        app.logger.error(e)
        db.session.rollback()
        return jsonify({"error": "company duplication"}), 400

    query = {
        "name": company_name[wanted_language],
        "language": wanted_language
    }
    instance, error = CompanyInfo.company_info_find_query(**query)
    if error:
        return jsonify({"error": "not found"}), 404

    return jsonify(instance.as_dict())
