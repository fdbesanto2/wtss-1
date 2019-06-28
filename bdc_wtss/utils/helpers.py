from bdc_wtss.utils.exceptions import APIError, BadRequestError
from flask import Response, json, request
from flask_restplus import Resource, utils
from functools import wraps
from jsonschema import validate, SchemaError, ValidationError, draft7_format_checker


def return_response(data, status_code, dumps=True):
    """
    Utility to render Flask Resource as JSON content type.
    :param data: Data to send
    :param status_code: HTTP Status code
    :param dumps: Flag to determines if data is already serialized
    :return: Flask Response
    """
    data = json.dumps(data) if dumps else data
    return Response(data, status_code, content_type='application/json')


def requires_model(schema):
    """
    Utility to require JSON schema object to validate request query arguments (request.args)

    Throws BadRequestError when occurs validation error.

    You can use it with APIResource in order to format BadRequestError output

    example:
    >>> from bdc_wtss.utils.helpers import requires_model
    >>> from flask import request, Flask
    >>>
    >>> app = Flask(__name__)
    >>>
    >>> coverage_schema = {
    >>>     "type": "object",
    >>>     "properties": {"coverage": {"type": "string"}}
    >>> }
    >>> @app.route('/')
    >>> @requires_model(coverage_schema)
    >>> def get_coverage():
    >>>     '''Now its safe to get coverage name'''
    >>>     coverage_name = request.args['coverage']
    >>>     return 'Coverage "{}" provided'.format(coverage_name)
    >>>
    >>> if __name__ == '__main__':
    >>>     app.run()

    :param schema: JSON Schema object
    """
    def decorator(fn):
        @wraps(fn)
        def decorated_function(*args, **kwargs):
            try:
                validate(instance=request.args, schema=schema, format_checker=draft7_format_checker)
            except (SchemaError, ValidationError) as e:
                raise BadRequestError(e.message)
            return fn(*args, **kwargs)
        return decorated_function
    return decorator


def response_model(schema):
    """
    Utility to require JSON Schema object on Flask Resource.
    :param schema: JSON Schema object
    :return: Formatted data according of JSON Schema
    """
    def decorator(fn):
        @wraps(fn)
        def decorated_function(*args, **kwargs):
            res, code, headers = utils.unpack(fn(*args, **kwargs))

            try:
                validate(instance=res, schema=schema)
            except (SchemaError, ValidationError) as e:
                # TODO: Should warning into stdout or just cascade exception?
                print('The response requires "{}" keys but got "{}"'.format(", ".join(schema["required"]), res))

            return res
        return decorated_function

    return decorator


class APIResource(Resource):
    """
    API Resource for Brazil Data Cube Modules (bdc)

    It aims to override `dispatch_request` member in order to
    handle status_code and error message through exception contexts.
    The exceptions must inherit from @APIError.

    TODO: Handle generic errors with same json syntax
    """
    def dispatch_request(self, *args, **kwargs):
        try:
            return super().dispatch_request(*args, **kwargs)
        except APIError as e:
            return return_response({
                "code": e.code,
                "message": e.message
            }, e.code)