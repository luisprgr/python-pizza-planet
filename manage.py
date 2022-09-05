import os
import pytest
from flask.cli import FlaskGroup
from flask_migrate import Migrate

import seeder

from app import flask_app
from app.plugins import db

# flake8: noqa
from app.repositories.models import Ingredient, Order, OrderDetail, Size


manager = FlaskGroup(flask_app)

migrate = Migrate()
migrate.init_app(flask_app, db)


@manager.command('test', with_appcontext=False)
def test():
    return pytest.main(['-v', './app/test'])


@manager.command('seeder')
def seed():
    seeder.execute_seeder()


@manager.command('hot-reload')
def hot_reload():
    os.environ.pop("FLASK_RUN_FROM_CLI")
    os.environ["FLASK_ENV"] = "development"
    flask_app.run(debug=True)


if __name__ == '__main__':
    manager()
