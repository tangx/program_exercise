#!/usr/bin/env python
# encoding: utf-8

"""
@version: 01
@author: 
@license: Apache Licence 
@python_version: python_x86 2.7.11
@site: https://www.uyinn.com
@software: PyCharm Community Edition
@file: subject_0016.py
@time: 2016/8/11 17:31
"""

'''
第 0016 题： 纯文本文件 numbers.txt, 里面的内容（包括方括号）如下所示：

[
    [1, 82, 65535],
    [20, 90, 13],
    [26, 809, 1024]
]


'''

import os
import openpyxl

excel_file = os.path.join('export', 'subject_0016.xlsx')


def main():
    numbers = open(os.path.join('resource', 'numbers.txt')).read()
    numbers_list = eval(numbers)

    wb = openpyxl.Workbook()
    ws = wb.active

    for l_num in numbers_list:
        ws.append(l_num)
        # print l_num

    wb.save(excel_file)


if __name__ == '__main__':
    main()
