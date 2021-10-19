#!/usr/bin/env Python
# -*- coding: utf-8 -*-
import pytest
import json

from app import app


@pytest.fixture
def api():
    return app.test_client()


def test_companies_get_params_check(api):
    resp = api.get(
        "/companies/Wantedlab", headers=[]
    )

    error_message = json.loads(resp.data.decode("utf-8"))
    assert resp.status_code == 404
    assert str(error_message['error']).find('wanted_language') > 0

    resp = api.get(
        "/companies/", headers=[("x-wanted-language", "ko")]
    )

    assert resp.status_code == 404
    assert str(resp.data).find('404 Not Found') > 0

    resp = api.post(
        "/companies",
        json={
            "company_name": {
                "ko": "라인 프레쉬",
                "tw": "LINE FRESH",
                "en": "LINE FRESH",
            },
            "tags": [
                {
                    "tag_name": {
                        "ko": "태그_1",
                        "tw": "tag_1",
                        "en": "tag_1",
                    }
                },
                {
                    "tag_name": {
                        "ko": "태그_8",
                        "tw": "tag_8",
                        "en": "tag_8",
                    }
                },
                {
                    "tag_name": {
                        "ko": "태그_15",
                        "tw": "tag_15",
                        "en": "tag_15",
                    }
                }
            ]
        },
        headers=[("x-wanted-language", "tw")],
    )

    resp = api.get(
        "/companies/LINE FRESH", headers=[("x-wanted-language", "ko")]
    )

    assert resp.status_code == 200
    company = json.loads(resp.data.decode("utf-8"))
    assert company == {
        "company_name": "라인 프레쉬",
        "tags": [
            "태그_1",
            "태그_8",
            "태그_15"
        ],
    }


def test_companies_post_params_check(api):
    resp = api.post(
        "/companies",
        json={
            "company_name": {},
            "tags": []
        },
        headers=[("x-wanted-language", "tw")],
    )

    assert resp.status_code == 400
    error_message = json.loads(resp.data.decode("utf-8"))
    assert str(error_message).find('company_name') > 0

    resp = api.post(
        "/companies",
        json={
            "company_name": {
                "ko": "테스트"
            },
            "tags": []
        },
        headers=[("x-wanted-language", "tw")],
    )

    assert resp.status_code == 404
    error_message = json.loads(resp.data.decode("utf-8"))
    assert str(error_message).find('not found') > 0
