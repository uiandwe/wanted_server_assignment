#!/usr/bin/env Python
# -*- coding: utf-8 -*-

from app import app, db
from flask import jsonify, request, make_response
from app.models.company import Company
from app.models.tag import Tag
from collections import defaultdict
from app.models.util import get_or_create


@app.route('/company/<companyName>', methods=['get'])
def get_company(companyName):
    wanted_language = request.headers.get('x-wanted-language', 'ko')

    # 검색
    try:
        company = Company.query.filter_by(name=companyName, language=wanted_language).first()
    except Exception as e:
        print(e)
        return jsonify({"error": "company not found"}), 400

    if not company:
        return jsonify({"error": "not found"}), 404

    # TODO 태그 리스트
    return jsonify(company.as_dict())


@app.route('/company', methods=['post'])
def create_company():
    wanted_language = request.headers.get('x-wanted-language', 'ko')

    if wanted_language == '':
        return jsonify({"error": "require x-wanted-language"}), 404

    # TODO 진짜 이렇게만 하면 되나?
    params_json = request.get_json()

    # 깔끔하게 할수 없나?
    try:
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

            instance, _ = get_or_create(db.session, Company, **d)

            for t in tag_name[language]:
                instance.tag.append(t)
            db.session.add(instance)

        db.session.commit()

    except Exception as e:
        print(e)
        return jsonify({"error": "company save error"}), 400

    try:
        company = Company.query.filter_by(name=company_name[wanted_language], language=wanted_language).first()
    except Exception as e:
        print(e)
        return jsonify({"error": "company not found"}), 400

    # 저장 후 출력
    if not company:
        return jsonify({"error": "not found"}), 404

    # TODO 태그 리스트
    return jsonify(company.as_dict())
