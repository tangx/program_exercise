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
    opener = urllib2.build_opener(urllib2.HTTPSHandler(),urllib2.HTTPHandler())
    cj = cookielib.CookieJar()
    cookie_support = urllib2.HTTPCookieProcessor(cj)
    opener.add_handler(cookie_support)

    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.76 Mobile Safari/537.36',
        'X-Forwarded-For': '171.212.113.133',  # 伪装IP地址
        'Accept': 'image/webp,image/*,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.8',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
    }

    header_list = []
    for key, value in headers.items():
        header_list.append((key, value))

    opener.addheaders = header_list

    return opener


def feng666_checkin(username, password):
    loginURI = 's.feng666.cc/auth/login'
    checkinURI = 's.feng666.cc/user/checkin'

    loginInfo = {
        'email': username,
        'passwd': password,
        'code': '',
        'remember_me': 'week',
    }
    login_paras = urllib.urlencode(loginInfo)
    opener = get_opener()

    try:
        # http mode
        loginURL = 'http://%s' % loginURI
        checkinURL = 'http://%s' % checkinURI

        opener.open(loginURL, login_paras)
        opener.open(checkinURL)

    except:
        # https mode
        loginURL = 'https://%s' % loginURI
        checkinURL = 'https://%s' % checkinURI
        try:
            opener.open(loginURL, login_paras)
            opener.open(checkinURL)
        except:
            pass


if __name__ == '__main__':
    username = 'your_email'
    password = 'your_password'
    feng666_checkin(username, password)
