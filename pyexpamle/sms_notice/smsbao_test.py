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
@FILE: smsbao_test.py
@time: 2016/7/11 21:37
"""

import os
import sys
import urllib
import hashlib


def md5hash(string):
    str_md5sum = hashlib.md5()
    str_md5sum.update(string)
    return str_md5sum.hexdigest()


def smsbao_send(user, password, phone, content):
    smsbao_send_url = ur'http://api.smsbao.com/sms?u=%s&p=%s&m=%s&c=%s' % (user, md5hash(password), phone, content)

    response_code = urllib.urlopen(smsbao_send_url).read()

    # print response_code
    pass


def main():
    username = 'JAZiiU'
    password = 'pCtSL1PeCsAp'
    phone_number = '18980624700'
    content = ur'hello,world. this is an test msg from python with smsbao.'
    smsbao_send(username, password, phone_number, content)



if __name__ == '__main__':
    main()
    # print md5hash('hello')

