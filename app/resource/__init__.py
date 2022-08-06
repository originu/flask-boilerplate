import fnmatch
import os

from flask import Blueprint
from flask_cors import CORS
from flask_restful import Api
from importlib import import_module

api_blueprint = Blueprint('api', __name__, url_prefix='/api')
CORS(api_blueprint)
api = Api(api_blueprint)

# add more blueprints
blueprints = [api_blueprint]

"""
load module dynamically from one-depth directory
"""
filter_expression = ['*_resource.py', '*_hook.py']
dir_list = os.listdir(__path__[0])
for dir_item in dir_list:
    if os.path.isdir(os.path.join(__path__[0], dir_item)):
        resource_files = fnmatch.filter(os.listdir("%s%s%s" % (__path__[0], os.sep, dir_item)), '*_resource.py')
        hook_files = fnmatch.filter(os.listdir("%s%s%s" % (__path__[0], os.sep, dir_item)), '*_hook.py')
        for module_file in (resource_files + hook_files):
            module_name = "%s.%s.%s" % (__package__, dir_item, module_file[0:-3])
            import_module(module_name)
pass

