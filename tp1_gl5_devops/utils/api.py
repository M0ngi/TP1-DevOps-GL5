import json

from flask import current_app
from requests import Response, get, post


def apiGet(route: str, data: dict | None = None, params: dict | None = None) -> tuple[Response, dict]:
    if data is None:
        data = {}
    if params is None:
        params = {}

    resp = get(
        current_app.config['API_PROXY'] + route,
        headers={'Content-type': 'application/json', 'Accept': 'text/plain'},
        data=json.dumps(data),
        params=params,
        timeout=5,
    )
    return resp, respJSON(resp)


def apiPost(route: str, params: dict | None = None) -> tuple[Response, dict]:
    if params is None:
        params = {}

    resp = post(
        current_app.config['API_PROXY'] + route,
        data=json.dumps(params),
        headers={'Content-type': 'application/json', 'Accept': 'text/plain'},
        timeout=5,
    )
    return resp, respJSON(resp)


def respJSON(resp: Response) -> dict:
    try:
        resp_data = json.loads(resp.content.decode())
    except Exception:
        resp_data = {}
    return resp_data
