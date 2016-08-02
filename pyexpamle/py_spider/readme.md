# python爬虫

## 1. 最基本抓站
使用正则
  1. [抓取服务器代理](./pyspider_s1_get_proxy.py)
  2. [抓取网站图片](./pyspider_s1_download_pics.py)

## 2. 使用代理服务器
  1. [http代理](./pyspider_s2_http_proxy.py)
  2. [代理有效性检查 http_proxy](./pyspider_s2_check_proxy.py)
    
## 3. 需要登录的情况 
    3.1 cookie的处理
    3.2 表单的处理
    3.3 伪装浏览器访问
    3.4 反"反盗链"
    3.5 终极绝招
## 4. 多线程并发抓取
## 5. 验证码处理
## 6. gzip/deflate支持
## 7. 更方便的多线程
    7.1 用twisted进行异步I/O抓取
## 8. 一些琐碎的经验
    8.1 连接池
    8.2 设定线程的栈大小
    8.3 设置失败自动重连
  + 设置超时
    > 在python2.6以后,可以直接在urllib/urllib2.openurl中设置timeout. 3秒超时` urllib2.urlopen(gg_url,timeout=3) `
    > 在python2.6以前,需要通过socket来设置, [参考链接](http://wiki.jikexueyuan.com/project/python-crawler/urllib2-use-details.html)
    8.5 登陆
## 9. 总结

[目录结构参考链接](http://wenku.baidu.com/link?url=KGeZwk8lKp6Mor5vkTjrikv1dSjLLhzBmNdHOYCMXGI42LRRKJFWLwB7Sc0LW8OhbBqN88gzOyrLbdGDwu3TDRRNUqZBvmRqpPVA2ox29km)