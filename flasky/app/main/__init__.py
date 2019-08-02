"""
Package main is for routers, so put all your router func in here
and public routers like index router could add below.
But I recommended just add some tools here
"""
import time
from functools import wraps

from flask import Blueprint, redirect, url_for, request, make_response, render_template
import json

from flasky.app import log
from flasky.app.models.commom_model import Session, User


def convert_to_strtime(form):
    strtime = (
        int(form['year']),
        int(form['month']),
        int(form['day']),
        0, 0, 0, 0, 0, 0
    )

    return time.mktime(strtime)


def current_user():
    if 'session_id' in request.cookies:
        session_id = request.cookies.get('session_id', 'guest')
        session = Session.find_by(session_id=session_id)
        if session is not None:
            user_id = session.user_id
            user = User.find_by(id=user_id)
            return user
        else:
            return None
    else:
        return None


def login_required(f):
    @wraps(f)
    def wrapper(*args):
        log('Check wheather logged')

        u = current_user()
        if u is None:
            return redirect(url_for('public.log_in'))
        else:
            return f(u)

    return wrapper


def load_form(form):
    return json.loads(json.dumps(form))


def response(template, cookie=None, **kwargs):
    t = template
    c = cookie

    re = make_response(render_template(t, **kwargs))
    if c is not None:
        for k, v in c.items():
            re.set_cookie(k, str(v))

    return re


main = Blueprint('main', __name__)

if __name__ == '__main__':
    test = dict(
        year=2010,
        month=1,
        day=1
    )
    print(convert_to_strtime(test))
