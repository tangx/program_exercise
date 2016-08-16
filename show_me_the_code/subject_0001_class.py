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

    def get_generator_code(self, lower=True, upper=False, digit=False, symbol=False, user_define=''):
        self.get_code_pool(lower, upper, digit, symbol, user_define)

        if self.code_length < len(self.code_pool):
            print ''.join(random.sample(self.code_pool, self.code_length))
        else:
            print "too long"


if __name__ == '__main__':
    iphone_gen = PromoteCodeGenerator()
    iphone_gen.gen_times = 1
    iphone_gen.code_length = 20
    iphone_gen.get_generator_code()
