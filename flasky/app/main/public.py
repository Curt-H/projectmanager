import json
import random
import time

from flask import Blueprint, render_template, request, redirect, url_for
from flasky.app.main import convert_to_strtime, login_required, response
from flasky.app.models.commom_model import User
from flasky.app.util import log, format_time

# from flasky.app.models.commom_model import Task

public = Blueprint('public', __name__)


@public.route('/', methods=['GET'])
@login_required
def index(user=None):
    u = user
    if u is None:
        u = {
            'username': 'GUEST',
        }

    return response('index.html', u=u)


@public.route('/log_in', methods=['GET'])
def log_in():
    return render_template('log_in.html')


@public.route('/validate_login', methods=['POST'])
def validate_login():
    un = request.form.get('username')
    pw = request.form.get('password')

    user = User.find_by(username=un)
    if user is None:
        return 'NO SUCH USER'
    elif pw != user.password:
        return 'WRONG PASSWORD'
    else:
        return redirect(url_for('public.index', u=user))
