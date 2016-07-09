#!/usr/bin/evn python
# encoding:utf-8
#
#  有道词典
#
import urllib
import re
import os
import sys


def main(word):
    youdaoDict_url = r'http://youdao.com/w/eng/%s/' % word
    content = urllib.urlopen(youdaoDict_url).read()

    dict_patt = r'<li>\w.*?</li>'

    patt = re.compile(dict_patt)

    results = patt.findall(content)

    for result in results:
        #
        # print result      //
        '''
        result=ur'<li>num. 一；一个</li>'

        分解步骤：
        result2=result.split('<li>')[1]
        设<li>为分隔符，对result进行分割，获得一个数组，取右边得result2
        result3=result2.rsplit('</li>')[0]
        设</li>为分隔符，对result2进行分割，获得一个数组，取左边得result3
        '''

        print "    %s" % result.split('<li>')[1].rsplit('</li>')[0]

    pass


if __name__ == "__main__":
    # sys.argv 是一个数组，包含文件本身所有变量。
    # py文件本身为sys.argv[0]
    
    if len(sys.argv) == 2:
        word = sys.argv[1]
        print "%s : " % word
        main(word)
