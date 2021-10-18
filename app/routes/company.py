#!/usr/bin/env Python
# -*- coding: utf-8 -*-

from app import app, db
from flask import jsonify, request, make_response
from app.models.company import Company


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
    # TODO 진짜 이렇게만 하면 되나?
    params_json = request.get_json()
    print(params_json)

    companies = []
    try:
        company_name = params_json.get('company_name', {})
        for language in company_name:
            print(language, company_name[language])
            company = Company(language=language, name=company_name[language])
            companies.append(company)
            db.session.add(company)

        db.session.commit()
        # company = Company.query.filter_by(name=companyName, language=wanted_language).first()
        #
        # post = Company(name=params_json['name'], author=current_user)
        # # 양식 처리 논리 Post는 데이터베이스에 새 레코드 삽입
        # db.session.add(post)
        # db.session.commit()

    except Exception as e:
        print(e)
        return jsonify({"error": "company save error"}), 400


    try:
        company = companies.filter_by(language=wanted_language).first()
    except Exception as e:
        print(e)
        return jsonify({"error": "company not found"}), 400

    # 저장 후 출력
    if not company:
        return jsonify({"error": "not found"}), 404

    # TODO 태그 리스트
    return jsonify(company.as_dict())
