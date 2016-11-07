#!/usr/bin/env python
# encoding: utf-8
#

"""
@version:  ??
@author: TangHsin
@license: Apache Licence
@mailto: octowhale@github
@site: 
@software: PyCharm Community Edition
@python ver: Python 2.7.12
@FILE: pyGetIpaddr.py
@time: 2016/11/5 11:34
"""

import os
import sys
import urllib2
import urllib
import re


def get_ipcn_result(ip=''):
    ipcn_url = 'http://ip.cn/index.php?ip=' + ip

    opener = urllib2.build_opener(urllib2.HTTPSHandler(), urllib2.HTTPSHandler())
    opener.addheaders = [('User-Agent', 'Chrome/46.0.2490.76')]

    content = opener.open(ipcn_url).read()

    return content


def get_ipaddr(ip=''):
    content = get_ipcn_result(ip)

    # ip_patt = r'<p>您查询的 IP：<code>(\d+.\d+.\d+.\d+)</code></p>'
    ip_patt = r' IP：<code>(\d+.\d+.\d+.\d+)</code></p>'
    ip_patt_compile = re.compile(ip_patt)

    try:
        return ip_patt_compile.findall(content)[0]
    except:
        return "请输入正确的 V4 IP 或 域名"


if __name__ == "__main__":
    # myip = '61.139.2.69'
    # print get_ipaddr(myip)
    # print get_ipaddr()

    print sys.argv

    try:
        print get_ipaddr(sys.argv[1])
    except:
        print get_ipaddr()
