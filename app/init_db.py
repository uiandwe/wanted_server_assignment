#!/usr/bin/env Python
# -*- coding: utf-8 -*-
import os

import click
from flask import current_app
from flask.cli import with_appcontext
from sqlalchemy import text

from app import db


def init_db():
    click.echo("init db")
    with current_app.open_resource(os.path.join(os.getcwd(), 'app/init_data/dump_company.sql')) as f:
        db.engine.execute(text(f.read().decode('utf8')).execution_options(autocommit=True))
        click.echo("insert company finish")
    with current_app.open_resource(os.path.join(os.getcwd(), 'app/init_data/dump_company_info.sql')) as f:
        db.engine.execute(text(f.read().decode('utf8')).execution_options(autocommit=True))
        click.echo("insert company_info finish")
    with current_app.open_resource(os.path.join(os.getcwd(), 'app/init_data/dump_tag.sql')) as f:
        db.engine.execute(text(f.read().decode('utf8')).execution_options(autocommit=True))
        click.echo("insert tag finish")
    with current_app.open_resource(os.path.join(os.getcwd(), 'app/init_data/dump_company_tag.sql')) as f:
        db.engine.execute(text(f.read().decode('utf8')).execution_options(autocommit=True))
        click.echo("insert company_tag finish")


@click.command('init-db')
@with_appcontext
def init_db_command():
    init_db()
    click.echo('Initialized the database.')


def init_app(app):
    app.cli.add_command(init_db_command)
