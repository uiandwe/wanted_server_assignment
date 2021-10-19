#!/usr/bin/env Python
# -*- coding: utf-8 -*-

from flask import jsonify, request
from sqlalchemy import and_

from app import app
from app.models.company_info import CompanyInfo
from app.validtors.search import SearchGetSchema
from app.models.language import Language


@app.route('/search', methods=['get'])
def search_index():
    parameter_dict = request.args.to_dict()
    wanted_language = request.headers.get('x-wanted-language', 'ko')
    search_keyword = parameter_dict.get('query', '')

    try:
        valid_data = {"search_keyword": search_keyword,
                      "wanted_language": wanted_language}
        error = SearchGetSchema().validate(data=valid_data)
        if error:
            raise ValueError(error)

        language_instance = Language.query.filter_by(name=wanted_language).one()
        company_infos = CompanyInfo.query.filter(
            and_(CompanyInfo.name.like('%' + search_keyword + '%'), CompanyInfo.language == language_instance)).all()
    except Exception as e:
        app.logger.error(e)
        return jsonify({"error": "company not found"}), 400

    if len(company_infos) == 0:
        return jsonify({"error": "not found"}), 404

    return jsonify([{"company_name": company_info.name} for company_info in company_infos])
