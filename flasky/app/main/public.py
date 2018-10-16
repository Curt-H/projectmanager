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
    tasks = Task.all()
    ts = []
    for i in range(len(tasks)):
        ts.append(tasks[len(tasks) - i - 1])
    log(tasks=ts)

    # load config.ini
    config = load_config()
    show_finished_item = config['show_finished_item']

    # V is a temprary value to make browser don't cache js when developing
    v = random.randint(0, 9999)
    return render_template('index.html', tasks=ts, v=v, sfi=show_finished_item)


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


@public.route('/showhide', methods=['GET'])
def task_show_hide():
    config = load_config()
    config['show_finished_item'] = not config['show_finished_item']
    save_config(config)

    return redirect(url_for('public.index'))
