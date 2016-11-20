#!/usr/bin/env python
# encoding: utf-8
#

"""
@version:  ??
@author: TangHsin
@license: Apache Licence
@mailto: octowhale@github
@site: 
@software: PyCharm Community Edition
@python ver: Python 2.7.12
@FILE: main.py.py
@time: 2016/11/20 11:03
"""

import os
import sys
import user_conf
import sqlite3
import imghdr
import hashlib
import qiniu


class QiniuImage:
    def __init__(self):
        self.access_key = user_conf.access_key
        self.secret_key = user_conf.secret_key
        self.bucket_name = user_conf.bucket_name
        self.bucket_url = user_conf.bucket_url
        self.image_prefix = user_conf.image_prefix
        self.image_db = user_conf.image_md5sum_db

    def to_open_database(self):
        '''
            open image database
        '''
        if not os.path.exists(self.image_db):
            # build a new one and return cx,cursor
            cx = sqlite3.connect(self.image_db)
            cursor = cx.cursor()
            sql = "create table qiniu_image_url ( image_md5sum varchar(32) primary key, image_type varchar(4), image_prefix varchar(50))"
            cursor.execute(sql)
            cx.commit()
            cx.close()

        # open it and return cx,cursor
        cx = sqlite3.connect(self.image_db)
        cursor = cx.cursor()
        return cx, cursor

    def to_close_database(self, cx):
        '''
            close the database
        '''
        # print " close database"
        cx.commit()
        cx.close()

    def to_search_database(self, cursor, image_md5):
        '''
            to serach the image if or not already in qiniu bucket
        '''
        sql = "select * from 'qiniu_image_url' where image_md5sum='%s';" % (image_md5)
        cursor.execute(sql)
        r = cursor.fetchall()
        # print r
        if len(r) == 1:
            return r[0]
        else:
            return None

    def to_update_database(self, cx, cursor, f_md5, f_pfix, f_type):
        '''
            update database after upload images to qiniu bucket
        '''
        # sql = "insert into qiniu_image_url values ('%s','%s','%s')"
        sql = "insert into qiniu_image_url values('%s','%s','%s')" % (f_md5, f_pfix, f_type)
        try:
            cursor.execute(sql)
            cx.commit()
        except:
            return None

    def to_check_file_type(self, f_file):
        '''
            check the file is or not a image file
        '''
        file_type = imghdr.what(f_file)
        return file_type

    def to_image_md5sum(self, f_file):
        '''
            to get the image md5sum code
        '''
        f = open(f_file, 'rb').read()
        f_md5 = hashlib.md5(f).hexdigest()
        return f_md5

    def to_upload_file(self, f_file, f_md5, f_type):
        '''
            to upload file into qiniu bucket
        '''
        try:
            # f_name = os.path.basename(f_file)
            q = qiniu.Auth(self.access_key, self.secret_key)

            # key means filename in qiniu bucket
            key = "%s%s.%s" % (self.image_prefix, f_md5, f_type)
            token = q.upload_token(self.bucket_name, key)

            qiniu.put_file(token, key, f_file)
            return True
        except:
            return False

    def to_output_url(self, f_file, b_url, pfix, f_md5, f_type):
        '''
            to print out qiniu image url
        '''
        f_name = os.path.basename(f_file)
        f_url = "http://%s/%s%s.%s" % (b_url, pfix, f_md5, f_type)
        print "%s" % (f_url)
        print "![%s](%s)" % (f_name, f_url)
        print '<img src="%s">%s</img>' % (f_url, f_name)
        print ""

    def to_main(self, f_list):
        cx, cr = self.to_open_database()
        # files = ['panda.png', '8-giant-panda-ailuropoda-melanoleuca-katherine-feng.jpg']
        for f_file in files:

            f_type = self.to_check_file_type(f_file)
            if f_type == None:
                # this file is not an image file.
                # goto next one
                # print "%s is not an image file" % f_file
                # print ""
                continue
            f_md5 = self.to_image_md5sum(f_file)

            # s_r = select_result
            s_r = self.to_search_database(cr, f_md5)
            # print s_r
            if s_r != None:
                # return image url
                # print "s_r=" % s_r
                f_pfix = s_r[1]
                # print s_r
                # print "![%s](%s%s%s.%s)" % (f_file, self.bucket_url, f_pfix, f_md5, f_type)
                self.to_output_url(f_file, self.bucket_url, f_pfix, f_md5, f_type)
                continue
            else:
                # upload file to qiniu

                if self.to_upload_file(f_file, f_md5, f_type):
                    # upload sucesss
                    # print "![%s](%s%s%s.%s)" % (f_file, self.bucket_url, f_pfix, f_md5, f_type)
                    self.to_output_url(f_file, self.bucket_url, self.image_prefix, f_md5, f_type)
                    # update database
                    self.to_update_database(cx, cr, f_md5, self.image_prefix, f_type)
                    continue
        else:
            self.to_close_database(cx)


if __name__ == "__main__":
    # files = ['panda.png', 'qiniu.db', '8-giant-panda-ailuropoda-melanoleuca-katherine-feng.jpg', 'user_conf.py']
    files = sys.argv[1:]
    q = QiniuImage()
    q.to_main(files)
