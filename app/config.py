#!/usr/bin/env Python
# -*- coding: utf-8 -*-
import os

from dotenv import load_dotenv

load_dotenv()

basedir = os.path.abspath(os.path.dirname(__file__))

db_host = os.environ['DB_HOST']
db_password = os.environ['DB_ROOT_PASSWORD']
db_user = os.environ['DB_USER']
db_port = os.environ['DB_PORT']
db_database = os.environ['DB_DATABASE']

database_uri = "{user}:{password}@{host}:{port}/{database}".format(user=db_user, password=db_password, host=db_host,
                                                                   port=db_port, database=db_database)


class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'xxA61AN7LsUvO3OyyfFsG4uK5GkPKOtQ7tOUlyCW3VHs3k_iCs8hWsLHBv65d')
    DEBUG = False


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://{db_uri}".format(db_uri=database_uri)
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://{db_uri}".format(db_uri=database_uri)
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    DEBUG = False


config = dict(
    dev=DevelopmentConfig,
    test=TestingConfig,
    prod=ProductionConfig
)

key = Config.SECRET_KEY
