import json
import random

from flask import Blueprint, render_template, request, redirect, url_for
from flasky.app.main import convert_to_strtime
from flasky.app import log
from flasky.app.models.task import Task

public = Blueprint('public', __name__)


def load_config():
    with open("config.ini", 'r', encoding='utf8') as f:
        config = json.load(f)
    log(config=config)
    return config


def save_config(config):
    with open("config.ini", 'w', encoding='utf8') as f:
        json.dump(config, f)
    log(config=config)


@public.route('/', methods=['GET'])
def index():
    # load all Tasks
    tasks = Task.all()

    return render_template('index.html', tasks=tasks)


@public.route('/new', methods=['GET'])
def task_new_view():
    tasks = Task.all()
    project = set()

    for t in tasks:
        project.add(t.project)

    log(project=project)
    return render_template('task_new.html', project=project)


@public.route('/new', methods=['POST'])
def task_new_add():
    form = json.loads(json.dumps(request.form))
    form['deadline'] = convert_to_strtime(form)
    log(form, type(form))

    Task.new(form)
    return redirect(url_for('.index'))


@public.route('/showhide', methods=['GET'])
def task_show_hide():
    config = load_config()
    config['show_finished_item'] = not config['show_finished_item']
    save_config(config)

    return redirect(url_for('public.index'))
