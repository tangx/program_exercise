#!/usr/bin/env python
# encoding: utf-8

"""
@version: ??
@author: HsinTangx
@license: Apache Licence 
@contact: uyinn28@gmail.com
@python_version: python_x86 2.7.11
@site: https://www.uyinn.com
@software: PyCharm Community Edition
@file: pyspider_s3_userLogin.py
@time: 2016/8/4 15:24
"""

import urllib2
import random
import pyspider_headers_list
import cookielib
import urllib


def zimuzuTV_login():
    username = 'Zz5Rkwu'
    password = 'HaMgC3h1w'
    loginUrl = 'http://www.zimuzu.tv/user/login'
    login_params = {'domain': 'zimuzu.tv', 'email': username, 'password': password}
    user_agent = random.choice(pyspider_headers_list.user_agent)
    headers = {'User-Agent': user_agent}

    cj = cookielib.LWPCookieJar()
    pro = urllib2.HTTPCookieProcessor(cj)
    opener = urllib2.build_opener(pro)
    urllib2.install_opener(opener)
    postData = urllib.urlencode(login_params)
    # req = urllib2.Request(loginUrl, data=, headers=headers)
    # loginResp = urllib2.urlopen(req)

    loginResp = opener.open(loginUrl, postData)
    print loginResp.read()

    signUrl = 'http://www.zimuzu.tv/user/sign'
    # signResp = urllib2.urlopen(signUrl, timeout=3)

    # print signResp.read()

    # signResp = opener.open(signUrl, timeout=3)
    # print signResp.read()


if __name__ == '__main__':
    zimuzuTV_login()
    pass
