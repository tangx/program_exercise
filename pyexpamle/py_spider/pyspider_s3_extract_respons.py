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
@file: pyspider_s3_extract_respons.py
@time: 2016/8/3 16:59

"""

'''
 参考文档:http://www.jianshu.com/p/2c2781462902
'''

import urllib2
from StringIO import StringIO
from gzip import GzipFile


def extract_gzip(resp):
    old_resp = resp
    data = resp.read()
    # print type(data)
    # print data
    # fileobj = StringIO(resp.read())
    fileobj = StringIO(data)
    fp = GzipFile(fileobj=fileobj, mode='r')
    # print fp
    resp = urllib2.addinfourl(fp=fp, headers=old_resp.headers, url=old_resp.url, code=old_resp.code)
    return resp


def gzip(data):
    fileobj = StringIO(data)
    data = GzipFile(fileobj=fileobj, mode='r')
    print data
    return data


def deflate(data):
    import zlib
    try:
        return zlib.decompress(data, -zlib.MAX_WBITS)
    except zlib.error:
        return zlib.decompress(data)


def extract_v2(resp):
    # old_resp = resp
    try:
        data = ''
        if resp.headers.get('content-encoding') == 'gzip':
            data = gzip(resp.read())
            # resp = urllib2.addinfourl(data, resp.headers, resp.url, resp.code)
        if resp.headers.get('content-encoding') == 'deflate':
            data = deflate(resp.read())
            # resp = urllib2.addinfourl(data, resp.headers, resp.url, resp.code)
        if data != '':
            resp = urllib2.addinfourl(data, resp.headers, resp.url, resp.code)
    except Exception as err:
        print err
        # resp = old_resp
    return resp


def extract(resp):
    data = resp.read()
    # print type(data)
    # print data
    try:
        # print len(data)
        if resp.headers.get('content-encoding') == 'gzip':
            data = gzip(data)
            # print data
        if resp.headers.get('content-encoding') == 'deflate':
            data = deflate(data)
            # print data
            # print len(data)
            # print resp.headers
            # print resp.url
            # print resp.code
            # resp = urllib2.addinfourl(fp=data, headers=resp.headers, url=resp.url, code=resp.code)
            # print type(data)
            # print resp.headers
            # print len(resp.read())
            # print dir(resp)
    except Exception as err:
        print err

    resp = urllib2.addinfourl(data, headers=resp.headers, url=resp.url, code=resp.code)
    # print resp.read()
    return resp


if __name__ == '__main__':
    abs_url = 'http://ip.cn/index.php?ip=8.8.8.8'
    # abs_url = 'https://www.baidu.com'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.76 Mobile Safari/537.36',
        # 'X-Forwarded-For': '8.8.8.8',  # 伪装IP地址
        'Accept': 'image/webp,image/*,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, sdch',  # 使用后压缩结果
        'Accept-Language': 'zh-CN,zh;q=0.8',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        # 'Content-Type': 'application/html',
    }
    # content = urllib2.urlopen(abs_url)
    url_request = urllib2.Request(abs_url, headers=headers)
    # content = urllib2.Request(abs_url)
    content = urllib2.urlopen(url_request)

    # content = extract_gzip(content)
    # content = extract(content)
    content = extract_v2(content)
    #
    print content.read()
    pass
