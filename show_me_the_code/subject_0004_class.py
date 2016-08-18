#!/usr/bin/env python
# encoding: utf-8

"""
@version: 01
@author: 
@license: Apache Licence 
@python_version: python_x86 2.7.11
@site: https://www.uyinn.com
@software: PyCharm Community Edition
@file: subject_0004_class.py
@time: 2016/8/17 10:51
"""

'''
第 0004 题：任一个英文的纯文本文件，统计其中的单词出现的个数。
'''

file_string = '''
@version: 01
@author:
@license: Apache Licence
@license: Apache Licence
@license: Apache Licence
@license: Apache Licence
@python_version: python_x86 2.7.11
@site: https://www.uyinn.com
@software: PyCharm Community Edition
@file: subject_0004.py
@time: 2016/8/10 18:45
'''

import os
import sys


class CountWordTimes:
    def __init__(self):
        self.filename = ''

    def file2str(self, filename):
        if type(filename) is str:
            file_string = filename
        else:
            file_string = open(filename).read()

        return file_string

    def count_word(self, filename):
        string = self.file2str(filename)

        words_list = string.split()

        for word in words_list:
            print "%s -> %s" % (word, words_list.count(word))


if '__main__' == __name__:
    counter = CountWordTimes()

    counter.count_word(file_string)


