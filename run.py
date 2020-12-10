# coding=utf-8

"""
@author: Reggie
@time:   2018/08/10 15:10
"""
import os
import sys
from . import create_app
from conf.config import config_dict, IP, PORT

app = create_app(config_dict['production'])

if __name__ == '__main__':
    print(app.url_map)
    app.run(host=IP, port=PORT)
