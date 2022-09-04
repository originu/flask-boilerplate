import logging
import os
from pathlib import Path

from flask import Flask

from .config import DefaultConfig
from .extension import db, migrate, jwt, bcrypt, kafka_consumer_listener
from .resource import blueprints
from .util import import_modules


def create_app(config=None, app_name="jedivin"):
    """
    :param config:
    :param app_name:
    :return:
    """
    app = Flask(app_name, instance_path=config.INSTANCE_DIRECTORY_PATH, instance_relative_config=True)
    configure_app(app)
    configure_blueprint(app)
    configure_extension(app)
    configure_error_handler(app)
    return app


def configure_app(app):
    # TO DO ITEM: fix configuration gracefully. kevin
    # http://flask.pocoo.org/docs/config/#instance-folders
    app.config.from_pyfile('production.cfg', silent=True)
    if app.config:
        # http://flask.pocoo.org/docs/api/#configuration
        app.config.from_object(DefaultConfig)

    if not os.path.exists(app.config['LOG_FOLDER']):
        os.makedirs(app.config['LOG_FOLDER'])
    logging.basicConfig(filename=os.path.join(app.config['LOG_FOLDER'], "debug.log"), level=logging.DEBUG)

    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])
    pass


def configure_blueprint(app):
    # import all of sub resource modules from this path
    path = Path(__file__).parent.absolute()
    import_modules(path, __package__, '*_resource.py')
    import_modules(path, __package__, '*_hook.py')

    """Configure blueprints in views."""
    for blueprint in blueprints:
        app.register_blueprint(blueprint)
    pass


def configure_extension(app):
    # for sqlalchemy
    db.init_app(app)

    # for flask migration, alembic
    migrate.init_app(app, db)
    # this is automatically to import entity modules so that you execute 'flask db migrate'
    path = Path(__file__).parent.absolute()
    import_modules(path, __package__, "*_entity.py")

    # for flask jwt
    jwt.init_app(app)

    # for flask bcrypt
    bcrypt.init_app(app)

    # kafka
    kafka_consumer_listener.init_app(app)
    pass


def configure_error_handler(app):
    pass
