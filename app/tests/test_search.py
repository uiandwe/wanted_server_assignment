#!/usr/bin/env Python
# -*- coding: utf-8 -*-
import pytest
import json

from app import app


@pytest.fixture
def api():
    return app.test_client()


def test_search_paramas(api):
    resp = api.get(
        "/search", headers=[("x-wanted-language", "ko")]
    )

    assert resp.status_code == 400
    error_message = json.loads(resp.data.decode("utf-8"))
    assert str(error_message['error']).find('not found') > 0

