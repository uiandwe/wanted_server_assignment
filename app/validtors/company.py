#!/usr/bin/env Python
# -*- coding: utf-8 -*-
from marshmallow import Schema, fields
from marshmallow.validate import Length


class CompanyPostSchema(Schema):
    company_name = fields.Dict(required=True, allow_none=False, validate=Length(min=1))
    tags = fields.List(fields.Dict())
    wanted_language = fields.Str(required=True, allow_none=False, validate=Length(2))


class CompanyGetSchema(Schema):
    company_name = fields.Str(required=True, allow_none=False, validate=Length(min=1))
    wanted_language = fields.Str(required=True, allow_none=False, validate=Length(2))
