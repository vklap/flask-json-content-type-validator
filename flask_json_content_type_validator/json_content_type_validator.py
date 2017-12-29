import flask
import functools


def validator(exception):
    """Validates that the request has a Content-Type header with application/json
    @param: exception A custom exception instance that will be raised if the validation fails
    """
    def _validator(f):
        @functools.wraps(f)
        def __validator(*args, **kwargs):
            content_type = flask.request.headers.get('Content-Type')
            if content_type != 'application/json':
                raise exception
            return f(*args, **kwargs)
        return __validator
    return _validator
