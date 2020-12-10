# *_*coding:utf-8 *_*

# @Author : Reggie
# @Time : 2020/12/10 下午 7:51 
# coding=utf-8
from flask import request
from .. import db
from api import api
from utils.gen_ret import RET, ret_jsonify


@api.route('/login', methods=['post'])
def login():
    """
    用户登录接口
    Type:
        application/json

    Args：
        name:   用户名
        pwd:    密码

    Return:
        {
        "code": 0,
        "msg": u"操作成功",
        "eng_msg": "successful"
        }
    """
    show_li = ['id', 'user_name']  # 返回值过滤
    index_map = {}
    name = request.json.get('name', '')
    pwd = request.json.get('pwd', '')
    if not all([name, pwd]):
        return ret_jsonify(RET.PARAMS_TYPE_ERR)
    index_map['user_name'] = name
    index_map['is_delete'] = 1
    ret = db.Find('info_user', indexMap=index_map, out=dict)
    if ret:
        if len(ret) == 1:
            if ret[0].get('password', '') == md5(pwd):
                ret = dict(filter(lambda x: x[0] in show_li, ret[0].items()))
                return ret_jsonify(data=ret)
            else:
                return ret_jsonify(RET.PASSWORD_ERROR)
        if len(ret) > 1:
            return ret_jsonify(RET.DATA_ERROR)
    else:
        return ret_jsonify(RET.LOGIN_FAILED)


@api.route('/sign', methods=['post'])
def sign():
    """
    注册接口
    Ages:
        name:   用户名
        pwd:    密码
    Return:
        {
        "code": 0,
        "msg": u"操作成功",
        "eng_msg": "successful"
        }
    """
    index_map = {}
    if not request.json:
        return ret_jsonify(RET.PARAMS_REQUIRED)
    name = request.json.get('name', '')
    pwd = request.json.get('pwd', '')
    if not all([name, pwd]):
        return ret_jsonify(RET.PARAMS_REQUIRED)
    index_map['user_name'] = name
    index_map['is_delete'] = 1
    ret = db.Find('info_user', indexMap=index_map, out=dict)
    if len(ret) > 0:
        return ret_jsonify(RET.USER_ALREADY_EXISTS)
    index_map['update_time'] = TimeNow()
    index_map['text_password'] = pwd
    index_map['password'] = md5(pwd)
    ret = db.Insert('info_user', index_map)
    if isinstance(ret, tuple) and ret[0] == 1:
        return ret_jsonify()
    else:
        return ret_jsonify(RET.REGISTER_USER_ERR)
