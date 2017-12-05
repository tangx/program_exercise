#!/usr/bin/env python
# encoding: utf-8

"""
@version: 01
@author: 
@license: Apache Licence 
@python_version: python_x86 2.7.11
@site: https://www.uyinn.com
@software: PyCharm Community Edition
@file: subject_0011_class.py
@time: 2016/8/18 9:50
"""

import os
import sys
import chardet

'''
    第 0011 题： 敏感词文本文件 filtered_words.txt，里面的内容为以下内容，当用户输入敏感词语时，则打印出 Freedom，否则打印出 Human Rights。
'''


class FilterWords:
    def __init__(self):
        self.filter_words_file = os.path.join("resource", "filtered_words.txt")
        # self.pool_list_utf8 = self.get_filter_words_list()
        self.pool_list_utf8 = open(self.filter_words_file, 'r').read().split()

    def get_filter_words_list(self):
        pool_list_utf8 = []
        for value in open(self.filter_words_file, 'r').read().split():
            # print chardet.detect(value)

            value = value.decode(encoding='utf-8')
            pool_list_utf8.append(value)
        return pool_list_utf8

    def is_filter(self, word):

        if word in self.pool_list_utf8:
            print "Freedom"
        else:
            print "Human Rights"


def main():
    pass


if __name__ == '__main__':
    main()

    s = '北京'
    # s = 'love'
    my_filter = FilterWords()
    my_filter.is_filter(s)

    my_filter.get_filter_words_list()

