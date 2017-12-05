#!/usr/bin/python3
#
# 第 0001 题：做为 Apple Store App 独立开发者，你要搞限时促销，
#    为你的应用生成激活码（或者优惠券），
#    使用 Python 如何生成 200 个激活码（或者优惠券）？
#

## random
# https://docs.python.org/3/library/random.html
  # random.choices 在 python3 中可用

## string
# https://docs.python.org/3/library/string.html

## 集合
# https://docs.python.org/3/tutorial/datastructures.html#sets
  # random.choice 不能用于 set 上

import random
import string

# 数字加字母
random_poll = string.ascii_letters + string.digits

# 非空白字符
# random_poll = set(string.printable) - set(string.whitespace)


def generate_promote_code(length):

    # print(random_poll)

    # random_list = [random.choice(random_poll) for _ in range(length)]
    # print(''.join(random_list))

    return ''.join([random.choice(random_poll) for _ in range(length)])


def generate_promote_code_choices(length):
    return ''.join(random.choices(random_poll, k=length))


def generate_times(times, length=10):
    # generate_promote_code(length)
    for _ in range(times):
        # print(generate_promote_code(length))
        print(generate_promote_code_choices(length))


if __name__ == '__main__':
    generate_times(10, 10)
    # print(random.choices(random_poll, k=10)
    # print(string.printable)
    print(random_poll)
