# coding=utf-8

"""
@author: Reggie
@time:   2018/08/10 23:33
"""

from flask import Blueprint

api = Blueprint('api', __name__)

import api.index
