#!/usr/bin/env python
# encoding: utf-8

"""
@version: 01
@author: HsinTangx
@license: Apache Licence
@python_version: python_x86 2.7.11
@site: https://www.uyinn.com
@software: PyCharm Community Edition
@file: pyspider_s3_feng666_sign.py
@time: 2016/8/4 17:49
"""

import cookielib
import urllib, urllib2


def get_opener():
    cj = cookielib.CookieJar()
    httpCooPorc = urllib2.HTTPCookieProcessor(cj)
    opener = urllib2.build_opener(httpCooPorc)

    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.76 Mobile Safari/537.36',
        # 'X-Forwarded-For': '8.8.8.8',  # 伪装IP地址
        'Accept': 'image/webp,image/*,*/*;q=0.8',
        # 'Accept-Encoding': 'gzip, deflate, sdch',  # 使用后压缩结果
        'Accept-Language': 'zh-CN,zh;q=0.8',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        # 'Content-Type': 'application/html',
    }

    header_list = []
    for key, value in headers.items():
        header_list.append((key, value))

    opener.addheaders = header_list

    return opener


def feng666_checkin(username, password):
    loginUrl = 'http://s.feng666.cc/auth/login'
    checkinUrl = 'http://s.feng666.cc/user/checkin'

    loginInfo = {
        'email': username,
        'passwd': password,
        'code': '',
        'remember_me': 'week',
    }
    login_paras = urllib.urlencode(loginInfo)
    opener = get_opener()

    # 登录
    loginResp = opener.open(loginUrl, login_paras, timeout=3)
    print loginResp.read()

    checkinResp = opener.open(checkinUrl, timeout=3)
    print checkinResp.read()


if __name__ == '__main__':

    username = 'your_email'
    password = 'your_password'
    feng666_checkin(username, password)
