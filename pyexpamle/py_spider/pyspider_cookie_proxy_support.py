#!/usr/bin/env python
# encoding: utf-8

"""
@version: 01
@author: 
@license: Apache Licence 
@python_version: python_x86 2.7.11
@site: https://www.uyinn.com
@software: PyCharm Community Edition
@file: pyspider_cookie_proxy_support.py
@time: 2016/8/5 20:18
"""

import urllib2
import cookielib


def main():
    http_url = 'http://ip.cn/'

    cj = cookielib.CookieJar()
    cookie_support = urllib2.HTTPCookieProcessor(cj)

    # http_proxy = {'http': '127.0.0.1:8087'}
    # proxy_support = urllib2.ProxyHandler(http_proxy)
    socks5_proxy = {'socks5': '127.0.0.1:36963'}
    proxy_support = urllib2.ProxyHandler(socks5_proxy)

    # opener = urllib2.build_opener(cookie_support, proxy_support, urllib2.HTTPHandler,urllib2.HTTPSHandler)

    # 生成 opener
    opener = urllib2.build_opener(urllib2.HTTPHandler, urllib2.HTTPSHandler)
    # 为 opener 追加支持
    opener.add_handler(proxy_support)
    # opener.add_handler(cookie_support)
    # 使用 opener
    urllib2.install_opener(opener)

    resp = urllib2.urlopen(http_url, timeout=3)

    print resp.read()


if __name__ == '__main__':
    main()
    pass
