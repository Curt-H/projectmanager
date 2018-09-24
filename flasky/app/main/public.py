import json

from flask import Blueprint, render_template, request, redirect, url_for
from flasky.app.main import convert_to_strtime
from flasky.app import log
from flasky.app.models.task import Task

public = Blueprint('public', __name__)


@public.route('/', methods=['GET'])
def index():
    ts = Task.all()
    log(tasks=ts)
    return render_template('index.html', tasks=ts)


@public.route('/new', methods=['GET'])
def task_new_view():
    return render_template('task_new.html')


@public.route('/new', methods=['POST'])
def task_new_add():
    form = json.loads(json.dumps(request.form))
    form['deadline'] = convert_to_strtime(form)
    log(form, type(form))

    t = Task.new(form)
    return redirect(url_for('.index'))
