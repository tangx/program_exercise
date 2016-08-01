#!/usr/bin/env python
# encoding: utf-8
#

"""
@version:  ??
@author: TangHsin
@license: Apache Licence
@mailto: uyinn28@gmail.com
@site: 
@software: PyCharm Community Edition
@FILE: pysmsbao.py
@time: 2016/7/11 16:59
"""

import os
import sys
import time
import urllib


def md5hash(str):
    import hashlib
    str_hash = hashlib.md5()
    str_hash.update(str)
    retrun
    return str_hash.hexdigest()


def response_check(res_code):
    response_dict = {
        0: ur'发送成功',
        30: ur'密码错误',
        40: ur'账号不存在',
        41: ur'余额不足',
        42: ur'账号过期',
        43: ur'IP地址限制',
        50: ur'内容还有敏感词',
        51: ur'手机号码不正确'
    }
    return response_dict[int(res_code)]


def smsbao_notice(user, pword, phone_num, content):
    # default_encoding='utf-8'
    # if sys.getdefaultencoding() != default_encoding:
    #     reload(sys)
    #     sys.setdefualtencoding(default_encoding)

    sms_user = user
    sms_pword = pword
    recive_phone = phone_num
    contents = content

    # ltime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime((time.time())))
    # time_content = ur'%s %s' % (ltime, contents)
    smsbao_url_send = ur'http://api.smsbao.com/sms?u=%s&p=%s&m=%s&c=%s' % (
        sms_user, sms_pword, recive_phone, contents)

    response_code = urllib.urlopen(smsbao_url_send).read()
    print response_check(response_code)


def smsbao_get_sms(phone, content):
    smsbao_url_get = ur'http://xxxx.xxx.xxx/xxx'
    smsbao_url_paras = ur'?m=%s&c=%s' % (phone, content)

    smsbao_full_url_get = ur'%s%s' % (smsbao_url_get, smsbao_url_paras)
    print smsbao_full_url_get


def smsbao_balance_check(sms_user, sms_pword):
    sms_pword = md5hash(sms_pword)
    balance_url = ur'http://www.smsbao.com/query?u=%s&p=%s' % (sms_user, sms_pword)
    response_code = urllib.urlopen(balance_url).read()
    print response_check(response_code)


def main():
    # smsbao_notice()

    smsbao_user = 'user_account'
    smsbao_pword = 'passowrd'
    recive_phone = '13900000000'
    content = 'main_something'

    smsbao_notice(smsbao_user, smsbao_pword, recive_phone, content)
    smsbao_balance_check(smsbao_user, smsbao_pword)
    smsbao_get_sms(recive_phone, content)


if __name__ == '__main__':
    main()
