# 笔记

## for k,v in dict

### 通用做法

```python
for i in d:
    print( i, d[i], d.get(i))
```


> https://stackoverflow.com/questions/26660654/how-do-i-print-the-key-value-pairs-of-a-dictionary-in-python

### python2 中

```python
for k, v in d.iteritems():
    print k, v
```

### python3 中

```python
for k, v in d.items():
    print(k, v)
```

## 读取文件的行

> https://docs.python.org/3.3/tutorial/inputoutput.html

```python

with open(filename, 'r') as fp:
    for line in fp:
        print(line)

```

`fp.readline()` 是读取一行。因此如果要循环读取文件的行，直接循环 `fp` 即可。 `fp` 本身就是一个生成器。