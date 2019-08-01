import json
import random
import time

from flask import Blueprint, render_template, request, redirect, url_for
from flasky.app.main import convert_to_strtime, login_required
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
        # ts = Task.all()
        # for t in ts:
        #     log(t.deadline)
        #     log(type(t.deadline))
        #     t.deadline = format_time(t.deadline, '[%Y-%m-%d-%a]')
        #     log(t.deadline)
        #
        # tasks = list()
        # projects = get_project_list()
        # for p in projects:
        #     for t in ts:
        #         if t.project == p:
        #             tasks.append(t)
        #
        # config = load_config()
        # v = random.randint(1, 10086)
        #
        return render_template('index.html', u=u, a='Hello world')


@public.route('/error', methods=['GET'])
def log_in():
    return 'WRONG'

    # def load_config():
    #     with open("config.ini", 'r', encoding='utf8') as f:
    #         config = json.load(f)
    #     log(config=config)
    #     return config

    # def save_config(config):
    #     with open("config.ini", 'w', encoding='utf8') as f:
    #         json.dump(config, f)
    #     log(config=config)

    # @public.route('/new', methods=['GET'])
    # def task_new_view():
    #     project = get_project_list()
    #
    #     log(project=project)
    #     return render_template('task_new.html', project=project)
    #
    #
    # @public.route('/new', methods=['POST'])
    # def task_new_add():
    #     form = json.loads(json.dumps(request.form))
    #     form['deadline'] = convert_to_strtime(form)
    #     form['creat_time'] = time.time()
    #     log(form, type(form))
    #
    #     Task.new(form)
    #     return redirect(url_for('.index'))
    #
    #
    # @public.route('/showhide', methods=['GET'])
    # def task_show_hide():
    #     config = load_config()
    #     config['show_finished_item'] = not config['show_finished_item']
    #     save_config(config)
    #
    #     return redirect(url_for('public.index'))
    #
    #
    # def get_project_list():
    #     tasks = Task.all()
    #     project = set()
    #     for t in tasks:
    #         project.add(t.project)
    #     return project
