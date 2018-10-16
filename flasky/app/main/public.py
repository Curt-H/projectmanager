import json
import random

from flask import Blueprint, render_template, request, redirect, url_for
from flasky.app.main import convert_to_strtime
from flasky.app import log
from flasky.app.models.task import Task

public = Blueprint('public', __name__)


@public.route('/', methods=['GET'])
def index():
    tasks = Task.all()
    ts = []
    for i in range(len(tasks)):
        ts.append(tasks[len(tasks) - i - 1])
    log(tasks=ts)

    # V is a temprary value to make browser don't cache js when developed
    v = random.randint(0, 9999)
    return render_template('index.html', tasks=ts, v=v)


@public.route('/new', methods=['GET'])
def task_new_view():
    return render_template('task_new.html')


@public.route('/new', methods=['POST'])
def task_new_add():
    form = json.loads(json.dumps(request.form))
    form['deadline'] = convert_to_strtime(form)
    log(form, type(form))

    Task.new(form)
    return redirect(url_for('.index'))
