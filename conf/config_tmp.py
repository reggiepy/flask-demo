# coding=utf-8

"""
@author: Reggie
@time:   2018/08/16 11:28
"""

import logging
import threading

IP = "0.0.0.0"
PORT = 7878

class Config(object):
    """BasicConfig"""
    _instance_lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        if not hasattr(Config, "_instance"):
            with Config._instance_lock:
                if not hasattr(Config, "_instance"):
                    Config._instance = object.__new__(cls)
        return Config._instance

    MANNA_DB_CONFIG =  {
        "host": "127.0.0.1",
        "port": 3306,
        "database": "manna",
        "user": "root",
        "password": "",
        "charset": "utf8",
    }


class DevelopmentConfig(Config):
    """开发环境配置类"""

    DEBUG = True
    LOG_LEVEL = logging.INFO


class ProductionConfig(Config):
    """生产环境配置类"""
    DEBUG = False
    LOG_LEVEL = logging.WARN


config_dict = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}
