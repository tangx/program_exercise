#!/usr/bin/python3
#
# **第 0003 题：**将 0001 题生成的 200 个激活码（或者优惠券）保存到 Redis 非关系型数据库中。
#

# from pyredis import Client

# client = Client(host="localhost")
# client.bulk_start()
# client.set('key1', 'value1')
# client.set('key2', 'value2')
# client.set('key3', 'value3')
# client.bulk_stop()
# [b'OK', b'OK', b'OK']

import sys

sys.path.append('/mnt/d/Documents/GitHub/program_exercise/show_me_the_code/')
sys.path.append(r'D:\\Documents\\GitHub\\program_exercise\\show_me_the_code\\')

from python3.s02 import s02
import pyredis

# print(s02.generate_promote_code(10))

client = pyredis.Client(host='localhost')


def put_keys():
    if client.ping():
        print('connected')
        client.bulk_start()
        for i in range(200):
            client.set('key{}'.format(i), s02.generate_promote_code(10))
        client.bulk_stop()


def get_keys():
    if client.ping():
        for i in range(200):
            # print(i)
            print(client.get('key{}'.format(i)))


if __name__ == "__main__":
    put_keys()
    get_keys()

    # client.get('key10')
    # client.get('key10')
    # client.get('key10')
    # client.get('key10')