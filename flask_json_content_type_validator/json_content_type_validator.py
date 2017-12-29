import flask
import functools


def validator(exception):
    def _validator(f):
        @functools.wraps(f)
        def __validator(*args, **kwargs):
            content_type = flask.request.headers.get('Content-Type')
            if content_type != 'application/json':
                raise exception
            return f(*args, **kwargs)
        return __validator
    return _validator
