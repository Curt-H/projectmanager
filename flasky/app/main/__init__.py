"""
Package main is for routers, so put all your router func in here
and public routers like index router could add below.
But I recommended just add some tools here
"""
from flask import Blueprint

main = Blueprint('main', __name__)
