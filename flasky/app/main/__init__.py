"""
Package main is for routers, so put all your router func in here
and public routers like index router could add below.
But I recommended just add some tools here
"""
from flask import Blueprint


def convert_to_strtime(form):
    strtime = [
        int(form['year']),
        int(form['month']),
        int(form['day']),
        0, 0, 0, 0, 0, 0
    ]

    return strtime


main = Blueprint('main', __name__)
