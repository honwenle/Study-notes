# Python学习笔记

## About
> 人生苦短，我用Python
- The Zen of Python `import this`
- 2 or 3 ?
- RECL or IDE ?

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