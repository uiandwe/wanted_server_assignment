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
