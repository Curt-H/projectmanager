"""
Package main is for routers, so put all your router func in here
and public routers like index router could add below.
But I recommended just add some tools here
"""
import time

from flask import Blueprint
import json


def convert_to_strtime(form):
    strtime = (
        int(form['year']),
        int(form['month']),
        int(form['day']),
        0, 0, 0, 0, 0, 0
    )

    return time.mktime(strtime)


def load_form(form):
    return json.loads(json.dumps(form))


main = Blueprint('main', __name__)

if __name__ == '__main__':
    test = dict(
        year=2010,
        month=1,
        day=1
    )
    print(convert_to_strtime(test))
