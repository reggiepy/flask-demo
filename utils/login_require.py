# coding=utf-8

"""
@author: Reggie
@time:   2018/08/11 14:53
"""
from flask import request, g
import functools

from .. import db
from utils.gen_ret import RET, ret_jsonify


def login_required(view_func):
    """登录验证装饰器"""

    @functools.wraps(view_func)
    def wrapper(*args, **kwargs):
        # 尝试从session中获取user_id
        user_id = request.json.get('user_id')
        result = db.query('select %s from info_user;')
        if result:
            # 用户已登录
            # 使用g变量临时保存user_id, g变量临时保存的内容可以在每个请求开始到请求结束的过程中使用
            # 这里使用g变量临时保存user_id，在后续的api代码中就不需要再次从session中获取user_id
            g.user_id = user_id
            return view_func(*args, **kwargs)
        else:
            # 用户未登录
            return ret_jsonify('', RET.EXCEPTION)

    return wrapper