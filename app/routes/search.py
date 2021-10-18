#!/usr/bin/env Python
# -*- coding: utf-8 -*-

from flask import jsonify, request
from sqlalchemy import and_

from app import app
from app.models.company import Company


@app.route('/search', methods=['get'])
def search_index():
    parameter_dict = request.args.to_dict()
    wanted_language = request.headers.get('x-wanted-language', 'ko')
    search_keyword = parameter_dict.get('query', '')

    if search_keyword == '':
        return jsonify({"error": "not found"}), 404

    try:
        companies = Company.query.filter(
            and_(Company.name.like('%' + search_keyword + '%'), Company.language == wanted_language)).all()
    except Exception as e:
        print(e)
        return jsonify({"error": "company not found"}), 400

    if len(companies) == 0:
        return jsonify({"error": "not found"}), 404

    return jsonify([{"company_name": company.name} for company in companies])
