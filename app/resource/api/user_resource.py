
from flask import jsonify
from app.resource import api_blueprint


@api_blueprint.route('/user/version', methods=['GET'])
def get_test1():
    return jsonify(version='0.1.0', name='jedivin')


@api_blueprint.route('/user/health', methods=['GET'])
def get_test2():
    return jsonify(status='normal', msg='it\'s normal')
