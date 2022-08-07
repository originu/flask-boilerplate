# -*- coding: utf-8 -*-
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
import logging

from app.constant.app_constant import INSTANCE_DIRECTORY_PATH

"""
datasource
"""
db = SQLAlchemy()


"""
logging
"""
logging.basicConfig(filename="logs/debug.log", level=logging.DEBUG)


"""
flaks migrate based on alembic
"""
migrate = Migrate()
