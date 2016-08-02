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
@file: pyspider_check_proxy.py
@time: 2016/8/2 10:58
"""

import urllib2


def check_proxy(proxy_addr, proxy_port, proxy_type):
    '''
        :这种方法可以使用socks代理
        :param proxy: '127.0.0.1:8087'
        :param protocol:  'http' or 'https' or 'socks5'
        :return:   success to return a dict , failed to return -1

    '''

    gg_url = 'http://ip.cn/'
    proxy = "%s:%s" % (proxy_addr, proxy_port)

    # 绑定代理
    url_handler = urllib2.ProxyHandler({proxy_type: proxy})
    opener = urllib2.build_opener(url_handler)
    urllib2.install_opener(opener=opener)

    try:
        content = urllib2.urlopen(gg_url, timeout=3)
        # print content.getcode()

        if content.getcode() == 200:
            # print proxy_type
            return {'proxy_addr': proxy_addr, 'proxy_port': proxy_port, 'proxy_type': proxy_type}

    except Exception:
        return -1


def check_socket_proxy(proxy_addr, proxy_port, proxy_type):
    '''
        :param proxy: '127.0.0.1:8087'
        :param protocol:  'http' or 'https'
        :return:   success to return a dict , failed to return -1

        报错处理: https://www.uyinn.com/scripts/python/python_socket_inet_pton_error.md
        参考文档: http://www.panweizeng.com/python-urllib2-socks-proxy.html
    '''

    import socket
    import socks
    # gg_url = 'http://ip.cn/'
    gg_url = 'http://www.bing.com'

    # print socks.PROXY_TYPES           # 字典{'SOCKS5': 2, 'SOCKS4': 1, 'HTTP': 3}
    # print socks.PROXY_TYPE_SOCKS5     # 2
    # print socks.PROXY_TYPE_SOCKS4     # 1
    # print socks.PROXY_TYPE_HTTP       # 3


    # 绑定代理
    # socks.set_default_proxy(proxy_type=proxy_type, addr=proxy_addr, port=proxy_port)
    socks.set_default_proxy(proxy_type=socks.PROXY_TYPES[proxy_type.upper()], addr=proxy_addr, port=proxy_port)
    socket.socket = socks.socksocket

    # 使用XX-NET-AGENT的HTTP代理的时候, 报错:
    # File "E:\Python27\lib\urllib2.py", line 558, in http_error_default
    # raise HTTPError(req.get_full_url(), code, msg, hdrs, fp)
    # urllib2.HTTPError: HTTP Error 400:

    # 封装一下头 待测试解决方法:
    # headers = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
    # urlreq = urllib2.Request(url="baidu.com", headers=headers)
    # req = urllib2.urlopen(urlreq)


    try:
        content = urllib2.urlopen(gg_url, timeout=3)
        # print content.getcode()
        if content.getcode() == 200:
            return {'proxy_addr': proxy_addr, 'proxy_port': proxy_port, 'proxy_type': proxy_type}

    except Exception:
        return -1


if __name__ == '__main__':
    # proxy = ur'127.0.0.1:8087'
    # protocol = ur'http'
    proxy_pool = ['127.0.0.1', 8087, 'http']
    # proxy_pool = ['127.0.0.1', 36963, 'socks5']
    proxy_addr = proxy_pool[0]
    proxy_port = proxy_pool[1]
    proxy_type = proxy_pool[2]
    # print check_proxy(proxy_addr, proxy_port, proxy_type)
    print check_socket_proxy(proxy_addr, proxy_port, proxy_type)
