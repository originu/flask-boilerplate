from flask import Blueprint
from flask_cors import CORS
from flask_restful import Api

api_blueprint = Blueprint('api', __name__, url_prefix='/api')
CORS(api_blueprint)
api = Api(api_blueprint)

# add more blueprints
blueprints = [api_blueprint]

