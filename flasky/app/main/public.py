from flask import Blueprint, render_template
from flasky.app.models.task import Task

public = Blueprint('public', __name__)


@public.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@public.route('/now', methods=['GET'])
def task_now():
    ts = Task.all()
    return ts
