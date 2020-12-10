# coding=utf-8

"""
@author: Reggie
@time:   2018/08/11 15:17
"""
from json import dumps
from flask import current_app, request


class RET:
    # 常用验证提示
    SUCCESS = {"code": 0, "msg": u"操作成功", "eng_msg": "successful"}
    EXCEPTION = {"code": 9999, "msg": u"异常错误", "eng_msg": "exception error"}
    UNKNOW = {"code": 9998, "msg": u"未知错误", "eng_msg": "unknow error"}
    ILLEGAL = {"code": 9997, "msg": u"非法请求", "eng_msg": "illegal error"}
    TOKEN_ERR = {"code": 9996, "msg": u"Token不正确或者已经过期", "eng_msg": "token has expired"}
    QUERY_NO_DATA = {"code": 9995, "msg": u"查询无任何数据", "eng_msg": "no data"}
    ATOM_ERR = {"code": 9994, "msg": u"原子封装信息错误", "eng_msg": "atom error"}
    AUTH_ERR = {"code": 9993, "msg": u"无访问权限", "eng_msg": "no access right"}
    NUM_ERR = {"code": 9992, "msg": u"loop_number必须为数字", "eng_msg": "no access right"}
    USER_ID_ERR = {"code": 9991, "msg": u"没有user_id", "eng_msg": "no access right"}

    # 请求参数提示
    PARAMS_TYPE_ERR = {"code": 8999, "msg": u"参数类型有误", "eng_msg": "param error"}
    PARAMS_REQUIRED = {"code": 8998, "msg": u"缺少必要的参数", "eng_msg": "param error"}
    PARAMS_FORMAT_ERR = {"code": 8997, "msg": u"参数格式不正确", "eng_msg": "param foramt error"}
    POST_FORMAT_ERR = {"code": 8996, "msg": u"POST数据格式不正确", "eng_msg": "post data error"}
    AGES_ERR = {"code": 8995, "msg": u"参数错误", "eng_msg": "post data error"}
    CHOICE_ONE_AGE = {"code": 8995, "msg": u"至少传入一个参数thing_type_id/thing_type", "eng_msg": "post data error"}

    COMPONENT_ID_ERR = {"code": 8995, "msg": u"生成component_id失败, 请检查参数：dtu_id、"
                                             u"alarm_host_no、loop_number、component_number",
                        "eng_msg": "post data error"}
    RESP_ERROR = {"code": 8994, "msg": u"没有收到数据", "eng_msg": "param error"}
    SUBMIT_TYPE_ERROR = {"code": 8993, "msg": u"'submit_type' ERROR", "eng_msg": "param error"}

    # 新增数据失败
    ADD_DATA_ERR = {"code": 7999, "msg": u"添加数据失败", "eng_msg": "add failed"}
    UPDATE_DATA_ERR = {"code": 7998, "msg": u"修改数据失败", "eng_msg": "modify failed"}
    DELETE_DATA_ERR = {"code": 7997, "msg": u"删除数据失败", "eng_msg": "delete failed"}
    UNIQUE_DATA_ERR = {"code": 7996, "msg": u"参数唯一性校验失败", "eng_msg": "param unique error"}
    EXIST_DATA_ERR = {"code": 7995, "msg": u"数据已存在", "eng_msg": "data exist"},
    CHECK_DATA_ERR = {"code": 7994, "msg": u"数据校验失败", "eng_msg": "check data failed"}

    # 登录相关
    LOGIN_FAILED = {"code": 6999, "msg": u"登录失败,用户名不存在", "eng_msg": "login failed"}
    ACCOUNT_BAN = {"code": 6998, "msg": u"账号已被禁用", "eng_msg": "account has been banned"}
    DATA_ERROR = {"code": 6997, "msg": u"后台数据错误，请联系管理员", "eng_msg": "data error"}
    USER_ALREADY_EXISTS = {"code": 6997, "msg": u"用户已存在", "eng_msg": "User already exists"}
    PASSWORD_ERROR = {"code": 6997, "msg": u"密码错误", "eng_msg": "User already exists"}

    # 用户相关
    UPDATE_PWD_ERR = {"code": 6998, "msg": u"修改密码失败", "eng_msg": "failed to change password"}
    UPDATE_USER_ERR = {"code": 6997, "msg": u"用户不能被停用", "eng_msg": "Users cannot be stopped"}
    DELETE_USER_ERR = {"code": 6996, "msg": u"用户不能被删除", "eng_msg": "Users cannot be delete"}
    REGISTER_USER_ERR = {"code": 6995, "msg": u"用户注册失败", "eng_msg": "Register error"}


def ret_jsonify(ret=RET.SUCCESS, data=''):
    if data:
        if isinstance(data, str):
            ret['data'] = data

        else:
            ret['data'] = data

    indent = None
    if current_app.config['JSONIFY_PRETTYPRINT_REGULAR'] \
            and not request.is_xhr:
        indent = 2
    return current_app.response_class(
        dumps(ret, indent=indent),
        mimetype='application/json')
