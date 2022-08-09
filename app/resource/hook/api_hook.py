from flask import request
from flask_jwt_extended import verify_jwt_in_request

from app.resource import api_blueprint


@api_blueprint.before_app_first_request
def before_app_first_request():
    pass


no_auth_paths = [
    '/api/server/health',
    '/api/server/version',
    '/api/auth/signin',
    '/api/auth/signup',
    '/api/auth/signout',
    '/api/auth/protected',
]


@api_blueprint.before_request
def before_request():
    # check JWT authentication
    is_no_auth_path = any(item in [request.path] for item in no_auth_paths)
    if not is_no_auth_path:
        verify_jwt_in_request()
    pass


@api_blueprint.teardown_request
def teardown_request(request):
    pass
