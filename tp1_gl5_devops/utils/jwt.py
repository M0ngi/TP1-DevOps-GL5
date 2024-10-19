import datetime
from functools import wraps
from typing import Any

import jwt
from flask import Response, current_app, flash, redirect, request, url_for

from tp1_gl5_devops.models.user import User
from tp1_gl5_devops.services.users import findOne
from tp1_gl5_devops.utils.http_response import error_response


def token_required(required: bool = True) -> Any:
    def token_verifier(f: Any) -> Any:
        def notAuthorized() -> Any:
            if required:
                flash('You must be logged in!')
                return redirect(url_for('web.login'))
            return redirect(url_for('web.home'))

        @wraps(f)
        def decorator(*args: Any, **kwargs: Any) -> Response:
            if (not request.cookies) == required:
                return notAuthorized()

            token = None
            if 'auth' in request.cookies:
                token = request.cookies.get('auth')

            if token is None:
                return notAuthorized()

            valid, current_user = isTokenValid(token)
            if valid != required:
                return notAuthorized()

            if required:
                return f(current_user, *args, **kwargs)

            return f(*args, **kwargs)

        return decorator

    return token_verifier


def api_token_required(f: Any) -> Any:
    def notAuthorized() -> Response:
        return error_response(error='Invalid access token', code=401)

    @wraps(f)
    def decorator(*args: Any, **kwargs: Any) -> Response:
        if not request.json:
            return notAuthorized()

        if 'auth' in request.json:
            token = request.json['auth']
        else:
            return notAuthorized()

        valid, current_user = isTokenValid(token)
        if not valid:
            return notAuthorized()

        return f(current_user, *args, **kwargs)

    return decorator


def createToken(user: User) -> str:
    return jwt.encode(
        {
            'user_id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=45),
        },
        current_app.config['SECRET_KEY'],
        'HS256',
    )


def isTokenValid(token: str) -> tuple[bool, User | None]:
    if not token:
        return False, None

    try:
        data = jwt.decode(token, current_app.config['SECRET_KEY'], algorithms=['HS256'])
        current_user = findOne(data['user_id'])

        if not current_user:
            raise Exception
    except Exception:
        return False, None

    return True, current_user
