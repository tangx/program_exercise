#!/usr/bin/env python
# encoding: utf-8

"""
@version: 01
@author: 
@license: Apache Licence 
@python_version: python_x86 2.7.11
@site: https://www.uyinn.com
@software: PyCharm Community Edition
@file: subject_0012.py
@time: 2016/8/10 21:00
"""

'''
    第 0012 题： 敏感词文本文件 filtered_words.txt，里面的内容 和 0011题一样，当用户输入敏感词语，则用 星号 * 替换，
    例如当用户输入「北京是个好城市」，则变成「**是个好城市」。

'''

import os
import sys

filter_file = os.path.join('resource', 'filtered_words.txt')


def get_filter_words(file):
    words_list = []
    f = open(file)
    for word in f.read().split():
        words_list.append(word.decode('utf-8'))
    return words_list


def sub_filter_words(stn):
    words_list = get_filter_words(filter_file)

    stn = stn.decode('utf-8')

    print len(stn)

    for f_word in words_list:
        if f_word in stn:
            # print 'in'
            stn = stn.replace(f_word, '*' * len(f_word))
    print stn


if __name__ == '__main__':
    stn = '北京是个好地方'
    sub_filter_words(stn)
    pass
