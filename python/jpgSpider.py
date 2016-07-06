#!/usr/bin/evn python
# encoding: utf-8
#
# 抓取百度贴吧的图片
#

import urllib
import re


def main():
    abs_url = r'http://tieba.baidu.com/p/4452126446'
    content = urllib.urlopen(abs_url).read()

    # re
    # re 的非贪婪匹配（最短匹配）说明
    # 问号（?）可以结束 pattern中通配符的贪婪模式，因此?必须跟在通配符（+/*)后面
    jpg_url = r'http://imgsrc.+?sign.*?.jpg'
    jpg_patt = re.compile(jpg_url)

    urls = jpg_patt.findall(content)

    for url in urls:
        print url

if __name__ == "__main__":
    main()
