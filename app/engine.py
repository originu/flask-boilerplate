import os

from flask import Flask

from .config import DefaultConfig
from .constant.app_constant import INSTANCE_DIRECTORY_PATH
from .extension import main_db_extension


def create_flask(config=None, app_name="jedivin"):
    """

    :param config:
    :param app_name:
    :return:
    """
    flask = Flask(app_name, instance_path=INSTANCE_DIRECTORY_PATH, instance_relative_config=True)
    configure_app(flask)
    configure_blueprint(flask)
    configure_extension(flask)
    configure_hook(flask)
    configure_error_handler(flask)
    configure_log(flask)
    return flask
    pass


def configure_app(flask):
    flask.config.from_object(DefaultConfig())

    if not os.path.exists(flask.config['UPLOAD_FOLDER']):
        os.makedirs(flask.config['UPLOAD_FOLDER'])
    pass


def configure_blueprint(flask):
    """Configure blueprints in views."""
    from app.resource.api import api_blueprint
    for bp in [api_blueprint]:
        flask.register_blueprint(bp)
    pass


def configure_extension(flask):
    main_db_extension.init_app(flask)
    pass


def configure_hook(flask):
    pass


def configure_error_handler(flask):
    pass


def configure_log(flask):
    pass