[![Build Status](https://travis-ci.org/vklap/flask-json-content-type-validator.svg?branch=master)](https://travis-ci.org/vklap/flask-json-content-type-validator)

# Flask JSON Content Type Validation Decorator

This package contains a Flask routes decorator that validates that the request 
has a Content-Type header with 'application/json'.

# Why?
Whenever you develop a Flask based API with plain vanilla flask routes that 
expect to get json data, then trying to access `request.get_json()` 
will return None whenever the Content-Type is not 'application/json' - which 
might eventually break your code. Using this decorator will help you keep your 
code clean and DRY.

# How it works?

## Create your custom exception

Below is an example of the exception you might wish to raise:

```python
class CustomError(Exception):
    def __init__(self, message, error_code):
        self.message = message
        self.error_code = error_code
```

## Register your custom error with a flask error handler

The decorator will throw your `CustomError` is the content type is not valid, 
in which case you can handle and return your customized response.

```python
@app.errorhandler(CustomError)
def custom_error_handler(custom_error):
    return flask.jsonify(dict(message=custom_error.message,
                                     error_code=custom_error.error_code)), 400
```

## Decorate your route with the content type validator

```python
import flask
from flask import request
from flask_json_content_type_validator import json_content_type_validator

app = flask.Flask(__name__)

@app.route('/echo-resource')
@json_content_type_validator.validator(
    CustomError(message='Missing Content-Type header application/json',
                error_code=1000)
)
def echo_resource():
    data = dict(**request.get_json())
    return flask.jsonify(data)

```
