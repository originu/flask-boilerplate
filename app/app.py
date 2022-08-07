import os
from pathlib import Path

from flask import Flask

from .config import DefaultConfig
from .constant.app_constant import INSTANCE_DIRECTORY_PATH
from .extension import db, migrate
from .resource import blueprints
from .util import import_modules


def create_app(config=None, app_name="jedivin"):
    """
    :param config:
    :param app_name:
    :return:
    """
    app = Flask(app_name, instance_path=INSTANCE_DIRECTORY_PATH, instance_relative_config=True)
    configure_app(app)
    configure_blueprint(app)
    configure_extension(app)
    configure_error_handler(app)
    configure_log(app)
    return app


def configure_app(app):
    app.config.from_object(DefaultConfig())
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
    db.init_app(app)
    migrate.init_app(app, db)

    # this is automatically to import entity modules so that you execute 'flask db migrate'
    path = Path(__file__).parent.absolute()
    import_modules(path, __package__, "*_entity.py")
    pass


def configure_error_handler(app):
    pass


def configure_log(app):
    pass
