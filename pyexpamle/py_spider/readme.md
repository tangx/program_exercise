# python爬虫

## 1. 最基本抓站
使用正则
  1. [抓取服务器代理](./pyspider_s1_get_proxy.py)
  2. [抓取网站图片](./pyspider_s1_download_pics.py)

## 2. 使用代理服务器
  1. [http代理](./pyspider_s2_http_proxy.py)
  2. [代理有效性检查 http_proxy](./pyspider_s2_check_proxy.py)
    
## 3. 伪装浏览器
### 3.1 cookie的处理
```python
import cookielib
import urllib
import urllib2

# 使用cookie
cj = cookielib.CookieJar()
pro = urllib2.HTTPCookieProcessor(cj)
opener = urllib2.build_opener(pro)

# 添加headers
# head_list=[('User-Agent',agent_value),('Accept-Language', 'zh-CN,zh;q=0.8')]
# opener.addheaders = header_list

# # # # # # # #

# 用户信息
# 以下内容为表单信息, 可以使用fiddle进行嗅探
login_para={
    'user':username,
    'passwd':passwd,
}
data=urllib.urlencode(login_para)

# 进行登录
resp=opener.open(url,data,timeout=3)
print resp.read()
```
[使用Fidder进行嗅探做爬虫签到](http://blog.csdn.net/u283056051/article/details/49946981) 

[zimuzu.tv 登录签到](./pyspider_s3_zimuzuTV_sign.py)

    3.2 表单的处理
    

### 使用headers
[使用header伪装浏览器](./pyspider_s3_request_headers.py)
```python
headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.76 Mobile Safari/537.36',
    'X-Forwarded-For': '8.8.8.8',  # 伪装IP地址
    'Accept': 'image/webp,image/*,*/*;q=0.8',
    # 'Accept-Encoding': 'gzip, deflate, sdch',  # 使用后压缩结果
    'Accept-Language': 'zh-CN,zh;q=0.8',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    # 'Content-Type': 'application/html',
}

url_request = urllib2.Request(abs_url, headers=headers)
# content = urllib2.Request(abs_url)
content = urllib2.urlopen(url_request)
```
    3.4 反"反盗链"
    3.5 终极绝招

## 4. 多线程并发抓取

## 5. 验证码处理

## 6. gzip/deflate支持
  1. [header中添加支持压缩](./pyspider_s3_request_headers.py)
  `headers{'Accept-Encoding':'gzip, deflate, sdch'}`
  2. [解压缩gzip/deflate](./pyspider_s3_extract_respons.py)

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

