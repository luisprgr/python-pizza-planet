from flask import jsonify
from functools import wraps


def service(service_function):
    @wraps(service_function)
    def wrapper(*args, **kwargs):
        items, error = service_function(*args, **kwargs)
        response = items if not error else {"error": error}
        status_code = 200 if items else 404 if not error else 400
        return jsonify(response), status_code

    return wrapper
