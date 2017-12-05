#!/usr/bin/env python
# encoding: utf-8

"""
@version: 01
@author: 
@license: Apache Licence 
@python_version: python_x86 2.7.11
@site: https://www.uyinn.com
@software: PyCharm Community Edition
@file: subject_0015.py
@time: 2016/8/11 17:22
"""
'''

第 0015 题： 纯文本文件 city.txt为城市信息, 里面的内容（包括花括号）如下所示：

{
    "1" : "上海",
    "2" : "北京",
    "3" : "成都"
}

'''
import openpyxl
import os

excel_file = os.path.join('export', 'subject_0015.xlsx')


def main():
    wb = openpyxl.Workbook()
    ws = wb.active

    city_file = os.path.join('resource', 'city.txt')
    s_city = open(city_file).read()
    d_city = eval(s_city)

    for key, value in d_city.items():
        print [key, value]
        ws.append([key, value])

    wb.save(excel_file)


if __name__ == '__main__':
    main()
    pass
