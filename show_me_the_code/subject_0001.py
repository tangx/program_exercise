#!/usr/bin/env python
# encoding: utf-8

"""
@version: 01
@author: 
@license: Apache Licence 
@python_version: python_x86 2.7.11
@site: https://www.uyinn.com
@software: PyCharm Community Edition
@file: subject_0001.py
@time: 2016/8/10 16:55
"""

'''
第 0001 题：做为 Apple Store App 独立开发者，你要搞限时促销，为你的应用生成激活码（或者优惠券），使用 Python 如何生成 200 个激活码（或者优惠券）？
'''

import random

lower_c = 'abcdefghijklmnopqrstuvwxyz'
digit_c = '1234567890'
symbol_c = '!@#$%^&*()_+-=<>?,./`~'


def get_random_code_util(pool, lenght):
    random_c_list = random.sample(pool, lenght)

    # 方法 1:
    # result = ''
    # for char in random.sample(pool_c, code_lenght):
    #     result += char

    # 方法 2:
    result = ''.join(random_c_list)

    # print result
    return result


def get_random_code(times=1, code_length=15, lower=True, upper=True, digit=True, symbol=False):
    pool_c = ''
    if lower is True:
        pool_c += lower_c
    if upper is True:
        pool_c += lower_c.upper()
    if digit is True:
        pool_c += digit_c
    if symbol is True:
        pool_c += symbol_c

    code_list = []
    for x in xrange(times):
        get_random_code_util(pool_c, code_length)
        code_list.append(get_random_code_util(pool_c, code_length))

    return code_list
if __name__ == '__main__':
    # print get_random_code(10, 20)
    pass
