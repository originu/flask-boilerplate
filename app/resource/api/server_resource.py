from flask import jsonify

import logging

from app.resource import api_blueprint


@api_blueprint.route('/server/version', methods=['GET'])
def get_version():
    logging.debug("Hello Kevin")
    return jsonify(version='0.1.0', name='jedivin')


@api_blueprint.route('/server/health', methods=['GET'])
def get_health():
    return jsonify(status='normal', msg='it\'s normal')
