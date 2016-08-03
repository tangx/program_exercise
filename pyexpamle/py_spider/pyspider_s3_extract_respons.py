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
    fileobj = StringIO(resp.read())
    fp = GzipFile(fileobj=fileobj, mode='r')
    resp = urllib2.addinfourl(fp=fp, headers=old_resp.headers, url=old_resp.url, code=old_resp.code)
    return resp


def gzip(data):
    file_obj = StringIO(data)
    return GzipFile(fileobj=file_obj, mode='r')


def deflate(data):
    import zlib
    try:
        return zlib.decompress(data, -zlib.MAX_WBITS)
    except zlib.error:
        return zlib.decompress(data)


def extract(resp):
    data = resp.read()

    if resp.headers.get('content-encoding') == 'gzip':
        data = gzip(data)
    if resp.headers.get('content-encoding') == 'deflate':
        data = deflate(data)

    resp = urllib2.addinfourl(data, resp.headers, resp.url, resp.code)

    return resp


if __name__ == '__main__':
    pass
