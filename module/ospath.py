#!/usr/bin/env python
# encoding: utf-8
#

"""
@version:  ??
@author: TangHsin
@license: Apache Licence
@mailto: uyinn28@gmail.com
@site: 
@software: PyCharm Community Edition
@FILE: ospath.py.py
@time: 2016/7/8 9:54
"""

print ur'http://python.usyiyi.cn/python_278/library/os.path.html'
import os
import sys


def main():
    filename = sys.argv[0]
    print filename
    cur_path = os.getcwd()

    print '\nbasename : 返回path上最后一个目录/文件名'
    print os.path.basename(cur_path)
    print os.path.basename(filename)

    print '\ndirname : 返回path上除开最后一个目录/文件的路径'
    print os.path.dirname(cur_path)
    print os.path.dirname(filename)

    print '\nexists : 目录/文件是否存在'
    print os.path.exists(filename)
    print os.path.exists(cur_path)

    print '\nlexists: 是否为绝对路径'
    print os.path.lexists(filename)
    print os.path.lexists(cur_path)

    print '\ngetsize 获取文件/目录大小'
    print os.path.getsize(filename)
    print os.path.getsize(cur_path)

    print '\nisfile 是否为文件'
    print os.path.isfile(filename)
    print os.path.isfile(cur_path)

    print '\nisdir 是否为目录'
    print os.path.isdir(filename)
    print os.path.isdir(cur_path)

    print '\nisabs 是否为绝对路径'
    print os.path.isabs(filename)
    print os.path.isabs(cur_path)

    print '\nismount 是否为挂载点'
    print os.path.ismount(filename)
    print os.path.ismount(cur_path)

    print '\njoin 路径联接'
    print os.path.join('c:\\', 'path1', 'path2', '')
    print os.path.join('c:', 'path1', 'path2')

    # new_path = os.path.join(os.getcwd(), 'e:', 'path1', 'path2')
    # print os.getcwd()
    # print 'new_path: %s ' % new_path
    # try:
    #     if not os.path.exists(new_path):
    #         os.makedirs(new_path)
    #     os.chdir(new_path)
    #     print os.getcwd()
    # except Exception as err:
    #     print err

    print '\nnormcase 目录路径优化'
    print '''    标准化路径名的大小写。在Unix和Mac OS X上，原样返回路径；
    在大小写不敏感的系统上，将路径名转换成小写。
    在Windows上，还会将斜线转换成反斜线。    '''
    print os.path.normcase(filename)
    print os.path.normcase(cur_path)


if __name__ == '__main__':


    main()
