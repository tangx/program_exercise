#!/usr/bin/env python
# encoding: utf-8

"""
@version: 01
@author: 
@license: Apache Licence 
@python_version: python_x86 2.7.11
@site: https://www.uyinn.com
@software: PyCharm Community Edition
@file: subject_0002.py
@time: 2016/8/10 18:05
"""
'''
第 0002 题：将 0001 题生成的 200 个激活码（或者优惠券）保存到 MySQL 关系型数据库中。
'''

import MySQLdb
import subject_0001

db_user = 'showme'
db_pass = 'the_code'
db_host = '192.168.56.10'
db_name = 'show_me_the_code'

def set_new_db_tables(cursor):
    SQL_CREATE_DB_SQL = 'create database if not EXISTS show_me_the_code DEFAULT CHARSET utf8 COLLATE utf8_general_ci;'
    SQL_CREATE_PROMOTE_TABLE = '''
            CREATE TABLE IF NOT EXISTS show_me_the_code.promote_code (
              idx int(100) NOT NULL AUTO_INCREMENT,
              code varchar(100) DEFAULT NULL,
              PRIMARY KEY (idx)
            ) ENGINE=MyISAM DEFAULT CHARSET=utf8;
        '''

    cursor.execute(SQL_CREATE_DB_SQL)
    cursor.execute(SQL_CREATE_PROMOTE_TABLE)

def set_code_in_mysql():
    conn = MySQLdb.connect(db_host, db_user, db_pass)
    cur = conn.cursor()

    # set_new_db_tables(cur)

    promote_code_list = subject_0001.get_random_code(10, 20)

    for value in promote_code_list:
        SQL_INSERT_CODE = "insert into show_me_the_code.promote_code set code='%s';" % value
        cur.execute(SQL_INSERT_CODE)

    conn.close()


if __name__ == '__main__':
    set_code_in_mysql()
    pass
