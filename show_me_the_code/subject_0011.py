#!/usr/bin/env python
# encoding: utf-8

"""
@version: 01
@author: 
@license: Apache Licence 
@python_version: python_x86 2.7.11
@site: https://www.uyinn.com
@software: PyCharm Community Edition
@file: subject_0011.py
@time: 2016/8/10 20:38
"""

'''
    第 0011 题： 敏感词文本文件 filtered_words.txt，里面的内容为以下内容，当用户输入敏感词语时，则打印出 Freedom，否则打印出 Human Rights。
'''

import os
import sys

if os.name == 'nt':
    filter_file = r'resource\filtered_words.txt'
else:
    filter_file = r'resource/filtered_words.txt'
filter_words = []

f = open(filter_file, 'r')

for word in f.read().split():
    filter_words.append(word.decode('utf-8'))

f.close()


def do_filter(word):
    print "%s --> " % word ,
    if word.decode('utf-8') in filter_words:
        print 'Freedom'
    else:
        print 'Human Rights'


def is_filter_words(args):
    for word in args:
        do_filter(word)


if __name__ == '__main__':
    print sys.argv
    if len(sys.argv) < 1:
        print 'not enough arguments'
        sys.exit(1)

    print sys.argv[1:]

    #
    # is_filter_words('北京')
    is_filter_words(sys.argv[1:])
    pass
