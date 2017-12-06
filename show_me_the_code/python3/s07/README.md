## UnicodeDecodeError: 'gbk' codec can't decode byte 0xac in position 27: illegal multibyte sequence

```python
#!/usr/bin/python3
# -*- coding:utf8 -*-
import codecs

with open("filename",'w',encoding="utf8") as fp:
    pass
```

> https://www.zhihu.com/question/22699590


## UnboundLocalError: local variable 'outter' referenced before assignment

如果不在函数体内使用 `global outter`， 如果反注释 `outter += 1 ` 则会报错， 这是 python 局部变量与全局变量的问题。

> http://c.biancheng.net/cpp/html/1827.html

```python
#!/usr/bin/python3

global outter
outter = 0

def main():
    global outter

    # outter += 1
    print(outter)

if __name__ == '__main__':
    main()

```

