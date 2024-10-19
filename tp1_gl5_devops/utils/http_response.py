from typing import Any

from flask import Response, jsonify, make_response


def error_response(error: Any, code: int) -> Response:
    return make_response(jsonify(error=error), code)


def valid_response(result: Any, code: int = 200) -> Response:
    return make_response(jsonify(result=result), code)
