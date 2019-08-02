import json
import random
import time

from flask import Blueprint, render_template, request, redirect, url_for, flash
from flasky.app.main import convert_to_strtime, login_required, response, validate_password
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


@public.route('/register', methods=['GET'])
def register(un='', pw=''):
    return response('register.html', un=un, pw=pw)


@public.route('/register', methods=['POST'])
def validate_register():
    un = request.form.get('username')
    pw = request.form.get('password')

    pw_check, wrong = validate_password(pw)
    if pw_check:
        flash('SUCCESS')
        return response('register.html', un=un, pw=pw)
    else:
        flash(f'[{wrong}] is a invalid word')
        return response('register.html', un=un, pw=pw)
