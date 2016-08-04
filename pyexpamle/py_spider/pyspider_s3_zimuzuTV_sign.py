#!/usr/bin/env python
# encoding: utf-8

"""
@version: 01
@author: HsinTangx
@license: Apache Licence
@contact: uyinn28@gmail.com
@python_version: python_x86 2.7.11
@site: https://www.uyinn.com
@software: PyCharm Community Edition
@file: zimuzuTV_sign.py
@time: 2016/8/4 16:03
"""

import urllib2
import urllib
import cookielib
from gzip import GzipFile
from StringIO import StringIO


def ungzip(data):
    try:
        file_obj = StringIO(data)
        data = GzipFile(fileobj=file_obj, mode='r')
    except:
        # print 'No need to ungzip'
        pass
    return data


# cookie opener
# 使用cookie访问
def get_opener(headers):
    cj = cookielib.CookieJar()
    pro = urllib2.HTTPCookieProcessor(cj)
    opener = urllib2.build_opener(pro)
    header = []
    for key, value in headers.items():
        elem = (key, value)
        header.append(elem)
    # print header
    opener.addheaders = header
    return opener


def zimuzuTV_sign(username, password):
    try:
        loginInfo = {
            'account': username,
            'password': password,
            # 'url_back': signUrl,
        }
    except ValueError:
        exit(1)

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

    opener = get_opener(headers)

    loginUrl = 'http://www.zimuzu.tv/User/Login/ajaxLogin'
    signUrl = 'http://www.zimuzu.tv/user/sign'

    # 签到
    try:
        # 登陆, 并获取cookie
        loginParas = urllib.urlencode(loginInfo)
        opener.open(loginUrl, loginParas, timeout=3)

        # 签到, 使用cookie登录
        signResp = opener.open(signUrl, timeout=3)
        data = signResp.read()
        # print data
    except Exception as err:
        print err


if __name__ == '__main__':
    username = 'xxxxxxxxx'
    password = 'wwwwwwwwww'
    zimuzuTV_sign(username, password)
