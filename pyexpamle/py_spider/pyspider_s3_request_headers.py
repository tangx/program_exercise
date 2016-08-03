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
@file: pyspider_s3_request_headers.py
@time: 2016/8/3 15:35
"""

import pyspider_s3_extract_respons


def extract_respons(resp):
    from gzip import GzipFile
    from StringIO import StringIO
    import urllib2
    # print type(resp)
    old_resp = resp
    if resp.headers.get('content-encoding') == 'gzip':
        gz = GzipFile(
            fileobj=StringIO(resp.read()),
            mode='r'
        )
        # resp = urllib2.addinfourl(gz, old_resp.headers, old_resp.url, old_resp.code)
        # resp.msg = old_resp.msg
        # # return resp

    if resp.headers.get('content-encoding') == 'deflate':
        gz = StringIO(deflate(resp.read()))
        # resp = urllib2.addinfourl(gz, old_resp.headers, old_resp.url, old_resp.code)
        # resp.msg = old_resp.msg

    resp = urllib2.addinfourl(gz, old_resp.headers, old_resp.url, old_resp.code)
    resp.msg = old_resp.msg
    return resp


def urllib2_headers():
    import urllib2
    abs_url = 'http://ip.cn/index.php?ip=8.8.8.8'
    # abs_url = 'https://www.baidu.com'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.76 Mobile Safari/537.36',
        'X-Forwarded-For': '8.8.8.8',  # 伪装IP地址
        'Accept': 'image/webp,image/*,*/*;q=0.8',
        # 'Accept-Encoding': 'gzip, deflate, sdch',  # 使用后压缩结果
        'Accept-Language': 'zh-CN,zh;q=0.8',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        # 'Content-Type': 'application/html',
    }
    # content = urllib2.urlopen(abs_url)
    url_request = urllib2.Request(abs_url, headers=headers)
    # content = urllib2.Request(abs_url)
    content = urllib2.urlopen(url_request)

    # print content.headers['Content-Encoding']
    # print content.headers.get('content-encoding')

    # content = extract_respons(content)
    # content = pyspider_s3_extract_respons.extract_gzip(content)
    # content=pyspider_s3_extract_respons.extract(content)
    try:
        content = pyspider_s3_extract_respons.extract(content)
    except:
        pass

    print content.read()
    print content.headers
    print dir(content)


def requests_headers():
    import requests
    abs_url = 'http://ip.cn/index.php'

    content = requests.get(abs_url)
    print type(content)
    print content.content
    print content.encoding
    print content.headers
    print dir(content)


if __name__ == '__main__':
    # requests_headers()
    urllib2_headers()
    pass
