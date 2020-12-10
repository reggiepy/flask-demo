# coding=utf-8

"""
@author: Reggie
@time:   2018/08/11 17:18
"""

from api import api


@api.route('/', methods=['get'])
def index():
    return "hello word!"
