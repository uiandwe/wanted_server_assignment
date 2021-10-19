#!/usr/bin/env Python
# -*- coding: utf-8 -*-
import pytest
import json

from app import app


@pytest.fixture
def api():
    return app.test_client()


def test_company2(api):
    assert 1 == 2
