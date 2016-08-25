#!/usr/bin/env python
# encoding: utf-8

"""
@version: 01
@author:
@license: Apache Licence
@python_version: python_x86 2.7.11
@site: https://www.uyinn.com
@software: PyCharm Community Edition
@file: s_0001.py
@time: 2016/8/16 17:00
"""

import random


class PromoteCodeGenerator:
    lower_c = 'abcdefghijklmnopqrstuvwxyz'
    digit_c = '0123456789'
    symbol_c = '!@#$%^&*()-_'
    code_pool = ''

    def __init__(self):
        self.gen_times = 10
        self.code_length = 10

    # def get_code_pool(self, lower=True, upper=False, digit=False, symbol=False, user_define=''):
    def get_code_pool(self, lower, upper, digit, symbol, user_define):

        if lower is True:
            self.code_pool += self.lower_c
        if upper is True:
            self.code_pool += self.lower_c.upper()
        if digit is True:
            self.code_pool += self.digit_c
        if symbol is True:
            self.code_pool += self.symbol_c

        self.code_pool += user_define

        return self.code_pool

    def get_code_with_random_sample(self, lower=True, upper=False, digit=False, symbol=False, user_define=''):
        '''
            random.sample(string,length)：
                1. 只能在string当中选择length个元素，每个有且只有一次被选中。
                2. length 的值不能大于 len(string)
        '''
        self.get_code_pool(lower, upper, digit, symbol, user_define)

        if self.code_length < len(self.code_pool):
            print ''.join(random.sample(self.code_pool, self.code_length))
        else:
            print "too long"

    def get_code_with_random_choice(self, lower=True, upper=False, digit=False, symbol=False, user_define=''):
        '''
            1. 通过string生成 code_pool
            2. random.choice(char) 选择一个元素，重复 N 次
            3. 通过 random.choice 方法，由于允许字符重复出现，生成的密码更随机，

        '''

        import string
        self.code_pool += user_define
        if lower is True:
            self.code_pool += string.lowercase
        if upper is True:
            self.code_pool += string.uppercase
        if digit is True:
            self.code_pool += string.digits
        if symbol is True:
            self.code_pool += self.symbol_c

        print ''.join([random.choice(self.code_pool) for i in xrange(self.code_length)])


if __name__ == '__main__':
    iphone_gen = PromoteCodeGenerator()
    iphone_gen.gen_times = 1
    iphone_gen.code_length = 20
    # iphone_gen.get_generator_code()
    iphone_gen.get_code_with_random_choice(True, True, True, False, '_+=')
