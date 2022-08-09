# -*- coding: utf-8 -*-
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

"""
datasource
"""
db = SQLAlchemy()


"""
flaks migrate based on alembic
"""
migrate = Migrate()


"""
JWT authentication
"""
jwt = JWTManager()


"""
encryption and decryption
"""
bcrypt = Bcrypt()
