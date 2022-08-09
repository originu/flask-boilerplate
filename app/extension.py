# -*- coding: utf-8 -*-
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
import logging

"""
datasource
"""
db = SQLAlchemy()


"""
flaks migrate based on alembic
"""
migrate = Migrate()
