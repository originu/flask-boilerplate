from flask import jsonify

from . import api_blueprint


@api_blueprint.route('/server/version', methods=['GET'])
def get_version():
    return jsonify(version='0.1.0', name='jedivin')


@api_blueprint.route('/server/health', methods=['GET'])
def get_health():
    return jsonify(status='normal', msg='it\'s normal')
