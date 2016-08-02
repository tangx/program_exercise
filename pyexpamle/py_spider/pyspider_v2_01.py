#!/usr/bin/env python
# encoding: utf-8
#

"""
@version:  01
@author: TangHsin
@license: Apache Licence
@mailto: uyinn28@gmail.com
@site: 
@software: PyCharm Community Edition
@FILE: pyspider_v2_01.py.py
@time: 2016/8/1 23:09
"""
'''
    参考文档
    install socks
    http://stackoverflow.com/questions/14820453/how-do-i-install-socks-socksipy-on-ubuntu
    http://www.panweizeng.com/python-urllib2-socks-proxy.html


'''
import os
import sys
import urllib2
# from ntlm import HTTPNtlmAuthHandler
# import pyspider_v1_01
import random

proxy_list = [
    {'ipaddr': '114.218.177.1', 'port': '8998'},
    {'ipaddr': '115.206.199.2', 'port': '8998'},
    {'ipaddr': '111.67.202.8', 'port': '808'},
    {'ipaddr': '112.23.96.2', 'port': '8123'},
    {'ipaddr': '114.215.192.1', 'port': '8118'},
    {'ipaddr': '1.27.203.2', 'port': '8118'},
    {'ipaddr': '106.38.251.6', 'port': '8088'},
    {'ipaddr': '117.135.250.8', 'port': '82'},
    {'ipaddr': '110.73.3.5', 'port': '8123'},
    {'ipaddr': '106.88.155.5', 'port': '8998'},
    {'ipaddr': '115.206.98.1', 'port': '8998'},
    {'ipaddr': '113.66.141.2', 'port': '8118'},
    {'ipaddr': '183.141.148.1', 'port': '3128'},
    {'ipaddr': '218.5.3.8', 'port': '8998'},
    {'ipaddr': '49.64.195.1', 'port': '8998'},
]

abs_url = r'https://www.uyinn.com/index'


def pyspider_http_proxy():
    # proxy_list = pyspider_v1_01.get_http_proxy()

    # proxy_dict = random.choice(proxy_list)
    # proxy = "%s:%s" % (proxy_dict['ipaddr'], proxy_dict['port'])

    proxy = ur'127.0.0.1:8087'  # 使用https代理
    urlhandle = urllib2.ProxyHandler({'http': proxy})
    opener = urllib2.build_opener(urlhandle)
    urllib2.install_opener(opener=opener)

    # print proxy

    abs_url = r'http://tieba.baidu.com/p/4452126446'
    content = urllib2.urlopen(abs_url)
    print content.headers
    print content.fp
    print content.getcode()
    print content.geturl()

    print dir(content)


def pyspider_socket_proxy():
    import socks
    import socket
    # socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, "127.0.0.1", 36963)
    # socket.socket = socks.socksocket
    #
    s = socks.socksocket()
    s.set_proxy(proxy_type=socks.PROXY_TYPE_SOCKS5, addr='127.0.0.1', port=36963)
    # content = urllib2.urlopen(abs_url).read()
    # print content
    print s.connect(('https://www.google.com', 443)).read()


if __name__ == '__main__':
    pyspider_http_proxy()
    # pyspider_socket_proxy()
