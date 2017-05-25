# Python学习笔记

## About
> 人生苦短，我用Python
- The Zen of Python `import this`
- 2 or 3 ?
- RECL or IDE ?
### 自省
- `help()`
- `dir()`
- `__doc__`
- *文档*
    * [官方网站](https://www.python.org/)
    * [官方文档](https://docs.python.org/3/)
    * [中文文档](http://docs.pythontab.com/)

## 数据类型
> computer是“她”
### num
- `id()` `type()`
- round四舍五入
- `dir(math)` `help(math)`
``` python
from __future__ import division
10//3 # 3
```

### str
- io
``` py
a = raw_input('please input :')
print 'your input is %s' % a
```
- 转义/原始
``` py
print "a\nb"
print r"a\nb"
```
- 索引 切片
``` py
str = "noclip"
str[2] # c
str.index('c') # 2
str[1:3] # oc
str[1:] # oclip
str[-2:] # ip
str[:-2] # nocl
str[1:-1:2] # ol
str[::-1] # pilcon
```
- 基本操作
    * `len()`、`count()`
    * `in`
    * `max`、`min`
    * `cmp`
    * `+` `*`
    
        ``` py
        'no' + 'clip' # noclip
        'noclip' * 2 # noclipnoclip
        ```
- 格式化
    * %
    * format
``` py
'xxx%.2fyyy' % 3.14159 # 3.14
'xxx%(a)s' % {'a':'noclip'} # xxxnoclip
'xxx{0}yyy{1}'.format(1.3,'noclip') # xxx1.3yyynoclip
'xxx{a}yyy{b}'.format(a='no', b='clip') # xxxnoyyyclip
```

- 常用方法
    * `isalpha`
    * `split`
    * `strip` `lstrip` `rstrip`
    * `upper` `lower` `capitalize` `isupper` `islower` `istitle`
    * `join`
        ``` py
        ','.join(['a','b'])
        ```

- 编码
    * `decode` `encode`
    * 避免乱码
``` py
# -*- coding: utf-8 -*-

unicode_str = unicode('中文', encoding='utf-8')
print unicode_str.encode('utf-8')

import codecs
codecs.open('filename', encoding='utf8')

a = u"中文"

# Python3
```

### list
- 操作与字符串一致
- `append()` `insert()`
- `extend()`
- `pop([i])` `remove()`
- `reverse()` `sort()`
``` py
li = [1,2]
li.append(3) # [1,2,3]
li[len(li):] = [4,5] # [1,2,3,4,5]
li.extend('67') # [1, 2, 3, 4, 5, '6', '7']
li.pop(2) # [1, 2, 4, 5, '6', '7']
li.remove(5) # [1, 2, 4, '6', '7']
```

### tuple
> Tuple与String一样，不可变，不可变，不可变
``` py
tp = (1,)
tp = (1,2,3)
```

### dict

- 构建
    * 字面量
    * 属性值
    * 键值对列表
``` py
obj = {}
obj['a'] = 'xxx'
obj = dict([['a',1],['b',2]])
```
- 常用
    * len(d)，返回字典(d)中的键值对的数量
    * d[key]，返回字典(d)中的键(key)的值
    * d[key]=value，将值(value)赋给字典(d)中的键(key)
    * del d[key]，删除字典(d)的键(key)项（将该键值对删除）
    * key in d，检查字典(d)中是否含有键为key的项
> HTML模板
``` py
temp = "<html><head><title>%(lang)s<title><body><p>My name is %(name)s.</p></body></head></html>"
my = {"name":"noclip", "lang":"python"}
temp % my
'<html><head><title>python<title><body><p>My name is qiwsir.</p></body></head></html>'
```

- copy 修改

### set
- 创建
    * `{[1,2,3]}`
    * `set("123")` `set([1,2,3])`
- 常用方法
    * add()
    * update()
    * pop() 任意剔除一个
    * remove() 指定剔除一个(不存的*会报错*)
    * discard() 指定剔除一个(不存的*不会报错*)
    * clear()
- 不可变frozenset()
- 运算
    * in
    * `set1 == set2` 、 `set1 != set2`
    * 子集`issubset()`超集`issuperset()` 并集`union()` 交集`intersection()` 差集`difference()`
``` py
{1,2,3} > {1,2} # TRUE
{1,2,3} > {1,4} # FALSE
{1,2} < {1,2,3} # TRUE

{1,2} | {2,3} # set([1, 2, 3])
{1,2} & {2,3} # set([2])
{1,2} and {2,3} # set([2])

{1,2,3} - {1,2} # set([3])
{1,2,3}.symmetric_difference({1,2,4}) # set([3, 4])
```

## 语句、文件

### 运算符
- 算数
- 比较
- 逻辑(布尔)

### 一般语句
- `print`
- `import`
- `=`
    * 多指 `a = 1,2`
    * 交换 `a, b = b, a`
    * 链式 `a = b = 1`
    * 增量 `a += 1`
### 条件语句
- `if` `elif` `else`
``` py
age = 2
if age > 18:
    print '已成年'
elif x > 0:
    print '未成年'
else:
    print '未出生'
```
- 三元
``` py
'1' if True else '0' # '1'
```
### 循环语句
- `for in`
``` py
for i in 'noclip':
    print i
```
- `range`
``` py
range(2) # [0,1]
range(1,3) # [1,2]
range(0,5,2) # [0,2,4]
range(0,-2,-1) # [0,-1]
```
- `zip`
``` py
zip([1,2],'abcd') # [(1, 'a'), (2, 'b')]
zip([1,2]) # [(1,), (2,)]
```
- `enumerate`
- 列表解析
``` py
[x**2 for x in range(5)] # [0, 1, 4, 9, 16]
['pre:'+x for x in 'noclip'] # ['pre:n', 'pre:o', 'pre:c', 'pre:l', 'pre:i', 'pre:p']
```

- `while`
> guess_number.py
- `while ... else` `for ... else`

### 文件
- `open` `write` `close`
- 模式
    * r *以读方式打开文件，可读取文件信息。*
    * w *以写方式打开文件，可向文件写入信息。如文件存在，则清空该文件，再写入新内容*
    * a *以追加模式打开文件（即一打开文件，文件指针自动移到文件末尾），如果文件不存在则创建*
    * r+ *以读写方式打开文件，可对文件进行读和写操作。*
    * w+ *消除文件内容，然后以读写方式打开文件。*
    * a+ *以读写方式打开文件，并把文件指针移到文件尾。*
    * b *以二进制模式打开文件，而不是以文本模式。该模式只对Windows或Dos有效，类Unix的文件是用二进制模式进行操作的。*
- `seek()` `tell()`
``` py
f = open('test.txt','a')
f.write('some text')
f.read()
for line in f:
    print line,
f.close()
with open("test.txt","a") as f:
    print f.read()
```
### 迭代
``` py
i = iter('noclip')
i.next()
```

## 函数
### 基本
- 经典的A+B
``` py
def plus_a_b(a, b):
    return a + b
plus_a_b(1, 2) # 3
```
- 文档
``` py
def fbnq(n):
    '''
    This is my Fibonacci
    '''
    a,b = 1,1
    for i in range(n):
        a,b = b,a+b
    return b
fbnq.__doc__
help(fbnq)
```
- 接受参数
    * 普通参数 `def foo(arg):`
    * 带默认值参数 `def foo(arg=1):`
    * 普通收集 `def foo(*arg):`
    * 键值收集 `def foo(**arg):`
- 传递参数
    * 顺序 `foo(1)`
    * 指定 `foo()` `foo(2)` `foo(arg=2)`
    * 元组解构 `foo(*arg)`
    * 字典解构 `foo(**arg)`
传入的可变变量在函数里修改是会修改原变量的
``` py
def foo(p1, p2, p3 = 3):
    print p1
    print p2
    print p3
foo(1,2,4)
foo(p1 = 1, p2 = 2, p3 = 4)
foo(*(1,2,3))
foo(**{'p1':1,'p2':2,'p3':3})
# *args **args
def foos(a, b = 2, *c, **d):
    print a
    print b
    print c
    print d
```
- 变量
    * 全局
    * 局部
- 命名空间
``` py
x = 1
print vars()
def a():
    x = 2
    print vars()
a()
print vars()
```

### 典型函数
- lambda
``` py
(lambda x: x**2)(3) # 9
```
- map
``` py
map(lambda x: x**2, range(5)) # [0, 1, 4, 9, 16]
map(lambda x: x*2, 'abc') # ['aa', 'bb', 'cc']
```
- reduce
``` py
# if py3
# from functools import reduce
reduce(lambda x,y: x*y, range(1,5)) # 24
```
- filter
``` py
filter(lambda x: x > 0, range(-5,5)) # [1, 2, 3, 4]
filter(lambda c: c!='i', 'noclip') # 'noclp'
```

## 类
``` py
class A(object):
    'this is class descript'
    def __init__(self, name):
        self.name = name
    def getName(self):
        return self.name
    def age(self, age):
        print "%s is %d" % (self.name, age)
a = A('noclip')
print A.__doc__
print a.name
print a.getName()
a.age(13)
```

## 模块

## 错误、异常

## 应用
### 数据
### 网站
### 计算