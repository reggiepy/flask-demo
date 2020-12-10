# coding=utf-8

"""
@author: Reggie
@time:   2018/08/10 15:10
"""
import logging
import os
from logging.handlers import RotatingFileHandler

from flask import Flask

from utils import db as DB

db = None
manna_db = None
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def set_logging(level):
    # 设置日志的记录等级
    logging.basicConfig(level=level)  # 调试debug级
    # 创建日志记录器，指明日志保存的路径、每个日志文件的最大大小、保存的日志文件个数上限
    file_log_handler = RotatingFileHandler(BASE_DIR + "/virt_device/logs/log", maxBytes=1024 * 1024 * 100,
                                           backupCount=10, encoding='utf-8')
    # 创建日志记录的格式                 日志等级    输入日志信息的文件名 行数    日志信息
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(filename)s:%(lineno)d %(message)s')
    # 为刚创建的日志记录器设置日志记录格式
    file_log_handler.setFormatter(formatter)
    # 为全局的日志工具对象（flask app使用的）添加日志记录器
    logging.getLogger().addHandler(file_log_handler)


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)

    set_logging(config.LOG_LEVEL)

    global db, nsq, manna_db
    db = DB.DB(config.DB_CONFIG)

    import api
    app.register_blueprint(api, url_prefix='/api')

    return app
