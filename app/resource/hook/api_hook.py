from flask import request

from app.resource import api_blueprint


@api_blueprint.before_app_first_request
def before_app_first_request():
    pass


@api_blueprint.before_request
def before_request():
    # request.data
    pass


# @api_blueprint.after_request
# def after_request(response):
#     return response


@api_blueprint.teardown_request
def teardown_request(request):
    pass
