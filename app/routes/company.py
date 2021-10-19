#!/usr/bin/env Python
# -*- coding: utf-8 -*-

from app import app, db
from flask import jsonify, request, make_response
from app.models.company import Company
from app.models.tag import Tag
from app.models.company_info import CompanyInfo
from collections import defaultdict
from app.models.util import get_or_create


@app.route('/companies/<companyName>', methods=['get'])
def get_company(companyName):
    # TODO 데코레이터로 안되나?
    wanted_language = request.headers.get('x-wanted-language', '')

    if wanted_language == '':
        return jsonify({"error": "require x-wanted-language"}), 404

    # 검색
    try:
        company_info = CompanyInfo.query.filter_by(name=companyName).first()
        company_info = CompanyInfo.query.filter_by(company=company_info.company, language=wanted_language).first()
    except Exception as e:
        app.logger.error(e)
        return jsonify({"error": "company not found"}), 404

    # TODO 태그 리스트
    return jsonify(company_info.as_dict())


@app.route('/companies', methods=['post'])
def create_company():
    wanted_language = request.headers.get('x-wanted-language', 'ko')

    if wanted_language == '':
        return jsonify({"error": "require x-wanted-language"}), 404

    # TODO 진짜 이렇게만 하면 되나?
    print(type(request.data))
    params_json = request.get_json()
    print(params_json)

    # TODO 깔끔하게 할수 없나? 함수로 빼기
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
    except Exception as e:
        app.logger.error(e)
        db.session.rollback()
        return jsonify({"error": "company duplication"}), 400

    # TODO 하나로 묶을수 있지 않을까?
    try:
        company_info = CompanyInfo.query.filter_by(name=company_name[wanted_language], language=wanted_language).first()
        print(company_info)
    except Exception as e:
        app.logger.error(e)
        return jsonify({"error": "company not found"}), 400

    if not company_info:
        return jsonify({"error": "not found"}), 404

    return jsonify(company_info.as_dict())
