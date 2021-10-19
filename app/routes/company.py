#!/usr/bin/env Python
# -*- coding: utf-8 -*-

from flask import jsonify, request
from sqlalchemy.orm.exc import NoResultFound

from app import app, db
from app.models.company import Company
from app.models.company_info import CompanyInfo
from app.models.tag import Tag
from app.validtors.company import CompanyPostSchema, CompanyGetSchema


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

    params_data = request.get_json()
    params_data['wanted_language'] = wanted_language

    error = CompanyPostSchema().validate(data=params_data)
    if error:
        return jsonify({"error": str(error)}), 400

    try:
        Company.create_company(params_data, Tag.create_tags, CompanyInfo.create_relation_company_info)
    except Exception as e:
        app.logger.error(e)
        db.session.rollback()
        return jsonify({"error": "company parameter error"}), 400

    company_name = params_data.get('company_name', {})
    query = {
        "name": company_name[wanted_language],
        "language": wanted_language
    }
    company_info_instance, error = CompanyInfo.company_info_find_query(**query)
    if error:
        return jsonify({"error": "not found"}), 404

    return jsonify(company_info_instance.as_dict())
