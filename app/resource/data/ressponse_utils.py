import string

from flask import abort, jsonify


def to_ok(body: dict = {}):
    msg = dict()
    msg["result"] = True
    msg["result_code"] = "000000"
    msg["result_message"] = ""
    msg["body"] = body
    return jsonify(msg)


def to_error(result_code: string, result_message: string, body: dict = {}):
    msg = dict()
    msg["result"] = False
    msg["result_code"] = result_code
    msg["result_message"] = result_message
    msg["body"] = body
    return jsonify(msg)


def to_abort_404():
    return abort(404)


def to_abort_500():
    return abort(500)
