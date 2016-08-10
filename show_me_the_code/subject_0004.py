#!/usr/bin/env python
# encoding: utf-8

"""
@version: 01
@author: 
@license: Apache Licence 
@python_version: python_x86 2.7.11
@site: https://www.uyinn.com
@software: PyCharm Community Edition
@file: subject_0004.py
@time: 2016/8/10 18:45
"""

'''
第 0004 题：任一个英文的纯文本文件，统计其中的单词出现的个数。
'''

file = '''
@version: 01
@author:
@license: Apache Licence
@python_version: python_x86 2.7.11
@site: https://www.uyinn.com
@software: PyCharm Community Edition
@file: subject_0004.py
@time: 2016/8/10 18:45
'''

import os


# 计算单词总数
def get_word_number(words_list):
    print len(words_list)


def get_word_times(words_list):
    words = []
    words_times = {}

    for word in words_list:
        if word not in words:
            words.append(word)
            # print ' %10s  ->  %d  times' % (word, words_list.count(word))
            words_times[word] = words_list.count(word)
    # print words_times
    return words_times


def count_words(filename):
    f = open(filename, 'r')
    content = f.read()

    words_list = content.split()

    # 计算单词总数
    get_word_number(words_list)

    # 计算单词出现次数
    get_word_times(words_list)

    f.close()


if __name__ == '__main__':
    filename = r'resource\world_war_i.txt'
    count_words(filename)

    pass
