#!/usr/bin/env python
# encoding: utf-8
#
#
import urllib
import re


def get_http_proxy():
    # abs_url=ur'http: // proxy.goubanjia.com / free / index.shtml'
    abs_url = r'http://www.kuaidaili.com/free/inha/'
    content = urllib.urlopen(abs_url).read()
    # print content

    ip_patt = r'\d+?\.\d+?\.\d+?\.\d+?'
    port_patt = r'PORT">\d+</td>'

    com_ip_patt = re.compile(ip_patt)
    com_port_patt = re.compile(port_patt)

    ip_list = com_ip_patt.findall(content)
    port_list = com_port_patt.findall(content)

    # for result in port_results:
    # print result.split('>')[1].rsplit('<')[0]

    # 因为 ip和port 不在同一行内，因此无法在同一个pattern中同时匹配。
    # 但，ip和port是一一对应关系，所以分别存入两个数组当中
    # 最后使用 i 为索引取得相应的 IP和port

    proxy_datas = []
    for i in xrange(len(ip_list)):
        # print "%s : %s" % (ip_list[i], port_list[i].split('>')[1].rsplit('<')[0])
        ipaddr = ip_list[i]
        port = port_list[i].split('>')[1].rsplit('<')[0]
        proxy_datas.append({'ipaddr': ipaddr, 'port': port})

    return proxy_datas


if __name__ == "__main__":

    proxy_datas = get_http_proxy()
    for proxy in proxy_datas:
        print proxy
