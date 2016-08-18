#!/usr/bin/evn python
# encoding: utf-8
#
# 抓取百度贴吧的图片
#

import urllib
import re

import os
import time

import thread
import threading

dir_path = r'G:\pic_down'


def main():
    abs_url = r'http://tieba.baidu.com/p/4452126446'
    content = urllib.urlopen(abs_url).read()

    # re
    # re 的非贪婪匹配（最短匹配）说明
    # 问号（?）可以结束 pattern中通配符的贪婪模式，因此?必须跟在通配符（+/*)后面
    jpg_url = r'http://imgsrc.+?sign.*?.jpg'
    jpg_patt = re.compile(jpg_url)

    urls = jpg_patt.findall(content)

    pic_down(urls, dir_path)


def pic_down(urls, dir_path):
    for url in urls:
        filename = os.path.join(dir_path, url.rsplit('/')[-1])
        # print url, '-->', filename

        time.sleep(1)
        print 'START %s --> %s ' % (url, filename)
        urllib.urlretrieve(url, filename=filename)
        # print '\tEND   %s --> %s ' % (url, filename)
        print '\tEND'


if __name__ == "__main__":
    main()
