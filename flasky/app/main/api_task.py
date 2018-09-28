from flask import Blueprint, request, jsonify
from flasky.app.models.task import Task

from flasky.app import log

api_task = Blueprint('api_task', __name__)


@api_task.route('/api/task/finish', methods=['POST'])
def api_task_finish():
    form = request.get_json()
    log(form, type(form))
    Task.delete_by(id=form['id'])

    result = 'finished'
    return jsonify(result)
