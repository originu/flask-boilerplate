import os

from app.constant.app_constant import INSTANCE_DIRECTORY_PATH


class BaseConfig(object):

    PROJECT = "jevivin"

    # Get app root path, also can use flask.root_path.
    # ../../config.py
    PROJECT_ROOT = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

    DEBUG = False
    TESTING = False

    ADMINS = ['youremail@yourdomain.com']

    # http://flask.pocoo.org/docs/quickstart/#sessions
    # SECRET_KEY = 'secret key'
    SECRET_KEY = '3d7572d6b9aa4b438afa056cc9938df27f4aa89092b3db332a68c56522ae8224'

    LOG_FOLDER = os.path.join(INSTANCE_DIRECTORY_PATH, 'logs')

    # Fild upload, should override in production.
    # Limited the maximum allowed payload to 16 megabytes.
    # http://flask.pocoo.org/docs/patterns/fileuploads/#improving-uploads
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024
    UPLOAD_FOLDER = os.path.join(INSTANCE_DIRECTORY_PATH, 'uploads')


class DefaultConfig(BaseConfig):

    DEBUG = False

    SENTRY_DSN = ""

    ENV = "development"     # development or production

    # Flask-Sqlalchemy: http://packages.python.org/Flask-SQLAlchemy/config.html
    SQLALCHEMY_ECHO = False
    # QLALCHEMY_TRACK_MODIFICATIONS adds significant overhead and will be
    # disabled by default in the future.
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    # SQLITE for local.
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:password@127.0.0.1:3306/jedivindb?charset=utf8'
    # MYSQL for production.
    #SQLALCHEMY_DATABASE_URI = 'mysql://username:password@server/db?charset=utf8'


class TestConfig(BaseConfig):
    TESTING = True
    CSRF_ENABLED = False
    WTF_CSRF_ENABLED = False

    SQLALCHEMY_ECHO = False
    # SQLALCHEMY_DATABASE_URI = 'sqlite://'
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:password@127.0.0.1:3306/jedivindb?charset=utf8'
