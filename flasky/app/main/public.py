import json

from flask import Blueprint, render_template, request

from flasky.app import log
from flasky.app.models.task import Task

public = Blueprint('public', __name__)


@public.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@public.route('/now', methods=['GET'])
def task_now():
    ts = Task.all()
    log(tasks=ts)
    return str(ts)


@public.route('/new', methods=['GET'])
def task_new_view():
    return render_template('task_new.html')


@public.route('/new', methods=['POST'])
def task_new_add():
    msg = json.dumps(request.form)
    log(msg)
    return msg
