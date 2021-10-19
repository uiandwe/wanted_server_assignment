#!/usr/bin/env Python
# -*- coding: utf-8 -*-
from marshmallow import Schema, fields
from marshmallow.validate import Length


class SearchGetSchema(Schema):
    search_keyword = fields.Str(required=True, allow_none=False, validate=Length(min=1))
    wanted_language = fields.Str(required=True, allow_none=False, validate=Length(2))
