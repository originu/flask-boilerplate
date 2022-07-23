# -*- coding: utf-8 -*-
from flask_sqlalchemy import SQLAlchemy

main_db_extension = SQLAlchemy()

import logging
logging.basicConfig(filename="logs/debug.log", level= logging.DEBUG)