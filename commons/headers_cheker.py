from functools import wraps
from flask import request
from os import environ


def secret_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        if 'X-AUTH-SECRET' in request.headers and \
                request.headers['X-AUTH-SECRET'] == environ.get("AUTH_SECRET"):
            return fn(*args, **kwargs)
        else:
            return {"error": "NO AUTH REQUEST"}, 401

    return wrapper


def admin_only(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        roles = request.headers.get('X-USER-ROLES')
        if {'1'}.issubset(_parse_role(roles)):
            return fn(*args, **kwargs)
        else:
            return {"error": "PERMISSION DENIED"}, 403
    return wrapper


def _parse_role(roles: str):
    return set(roles.split(";"))
