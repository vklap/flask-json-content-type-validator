import flask
from flask import request
from flask_json_content_type_validator import json_content_type_validator


class CustomError(Exception):
    def __init__(self, message, error_code):
        self.message = message
        self.error_code = error_code


app = flask.Flask(__name__)


@app.route('/echo-resource')
@json_content_type_validator.validator(
    CustomError(message='Missing Content-Type header application/json',
                error_code=1000)
)
def echo_resource():
    data = dict(**request.get_json())
    return flask.jsonify(data)


@app.errorhandler(CustomError)
def custom_error_handler(custom_error):
    return flask.jsonify(dict(message=custom_error.message,
                                     error_code=custom_error.error_code)), 400
