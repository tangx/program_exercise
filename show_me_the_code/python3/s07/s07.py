#!/usr/bin/python3
# -*- coding:utf8 -*-
#
# **第 0007 题：**有个目录，里面是你自己写过的程序，统计一下你写过多少行代码。包括空行和注释，但是要分别列出来。
#

import os
# import sys
import re

# path = os.path.abspath(os.curdir)
# path = r'D:\Documents\GitHub\program_exercise\show_me_the_code\python3\s07'
path = r'/mnt/d/Documents/GitHub/program_exercise/show_me_the_code/python3/s07'
# path = r'/mnt/d/Documents/GitHub/program_exercise/show_me_the_code/'

# re pattern
re_blank_line = re.compile(r'^\s*$')
re_comment_line = re.compile(r'^\s*#')
re_code_line = re.compile(r'^\s*\w')

# init
blank_line_count = 0
comment_line_count = 0
code_line_count = 0


def path_walk(path):

    for cur_path, dirs, files in os.walk(path):
        for file in files:
            # print(os.path.join(cur_path, file))
            ext = file.split('.')[-1]
            if ext == 'py'.lower():
                if file == 'init.py':
                    continue
                count(os.path.join(cur_path, file))
                # print(os.path.join(cur_path, file))

        for dir in dirs:
            path_walk(os.path.join(cur_path, dir))


def count(file):

    global code_line_count
    global blank_line_count
    global comment_line_count

    with open(file, 'r', encoding='utf-8') as fp:
        for line in fp:
            if re_blank_line.search(line):
                blank_line_count += 1
                continue
            
            if re_comment_line.search(line):
                comment_line_count += 1
                # print(line)
                continue

            code_line_count += 1


def main():

    path_walk(path)

    print('blank_line_count = {}'.format(blank_line_count))
    print('comment_line_count = {}'.format(comment_line_count))
    print('code_line_count = {}'.format(code_line_count))

if __name__ == '__main__':
    main()
