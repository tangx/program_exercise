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


def check_http_proxy(proxy, protocol):
    '''
        :param proxy: '127.0.0.1:8087'
        :param protocol:  'http' or 'https'
        :return:   success to return a dict , failed to return -1
    '''

    gg_url = 'http://ip.cn/'

    url_handler = urllib2.ProxyHandler({protocol: proxy})
    opener = urllib2.build_opener(url_handler)
    urllib2.install_opener(opener=opener)

    try:
        content = urllib2.urlopen(gg_url, timeout=3)
        # print content.getcode()

        if content.getcode() == 200:
            return {'proxy': proxy, 'protocol': protocol}
        else:
            return -1
    except Exception:
        return -1


if __name__ == '__main__':
    # proxy = ur'127.0.0.1:8087'
    # protocol = ur'http'
    proxy_pool = ['127.0.0.1:8087', 'http']
    proxy = proxy_pool[0]
    protocol = proxy_pool[1]
    print check_http_proxy(proxy, protocol)
    pass
