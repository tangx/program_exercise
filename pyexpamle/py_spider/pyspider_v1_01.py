#!/usr/bin/env python
# encoding: utf-8
#
#
import urllib
import re


def main():
    abs_url = r'http://www.kuaidaili.com/free/inha/'
    content = urllib.urlopen(abs_url).read()
    # print content

    ip_patt = r'\d+?\.\d+?\.\d+?\.\d+?'
    port_patt = r'PORT">\d+</td>'

    com_ip_patt = re.compile(ip_patt)
    com_port_patt = re.compile(port_patt)
    ip_results = com_ip_patt.findall(content)
    port_results = com_port_patt.findall(content)

    # for result in port_results:
        # print result.split('>')[1].rsplit('<')[0]

    # 因为 ip和port 不在同一行内，因此无法在同一个pattern中同时匹配。
    # 但，ip和port是一一对应关系，所以分别存入两个数组当中
    # 最后使用 i 为索引取得相应的 IP和port

    for i in xrange(len(ip_results)):
        print "%s : %s" % (ip_results[i], port_results[i].split('>')[1].rsplit('<')[0])

    print ip_results


if __name__ == "__main__":
    main()
    print "end"
