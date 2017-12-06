#!/usr/bin/python3
#
# **第 0004 题：**任一个英文的纯文本文件，统计其中的单词出现的个数。
#

import os

filename = 'cpp.log'

print(os.path.abspath(os.curdir))


def count(filename):
    count_dict = {}
    with open(filename, 'r') as fp:
        # for line in fp.readline:  # 这个是直接取一行。
        for line in fp:    # 如果要单独取行，不需要 readline
            # print(line)
            for word in line.split(' '):
                if count_dict.get(word) is None:
                    count_dict[word] = 1
                else:
                    count_dict[word] += 1

    # for k in count_dict:
        # print(k, count_dict.get(k))

    for k, v in count_dict.items():
        print(k, v)


if __name__ == "__main__":
    count(filename)
