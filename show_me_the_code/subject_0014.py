#!/usr/bin/env python
# encoding: utf-8

"""
@version: 01
@author: 
@license: Apache Licence 
@python_version: python_x86 2.7.11
@site: https://www.uyinn.com
@software: PyCharm Community Edition
@file: subject_0014.py
@time: 2016/8/11 10:45
"""

'''
第 0014 题： 纯文本文件 student.txt为学生信息, 里面的内容（包括花括号）如下所示：

{
    "1":["张三",150,120,100],
    "2":["李四",90,99,95],
    "3":["王五",60,66,68]
}

'''

import os
import openpyxl

file_student_info = os.path.join('resource', 'student.txt')
excel_file = os.path.join('export', 'subject_0014.xlsx')


def get_info(file):
    return open(file).read()


def save_in_excel(l_infos):
    wb = openpyxl.Workbook()
    ws = wb.active

    for l_info in l_infos:
        ws.append(l_info)

    wb.save(excel_file)


def dict2list(d_info):
    l_info = []
    for key, value in d_info.items():
        # print key, value
        value.insert(0, key)
        l_info.append(value)
    return l_info


def main():
    s_info = get_info(file_student_info)

    # 字符串转字典
    d_info = eval(s_info)

    # 字典转list
    l_info = dict2list(d_info)

    # 保存文件
    save_in_excel(l_info)


if __name__ == '__main__':
    main()
    pass
