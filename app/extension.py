# -*- coding: utf-8 -*-
from flask_sqlalchemy import SQLAlchemy
import logging


"""
datasource
"""
main_db_extension = SQLAlchemy()


"""
logging
"""
logging.basicConfig(filename="logs/debug.log", level=logging.DEBUG)
