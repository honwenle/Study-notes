# Python学习笔记

## About
> 人生苦短，我用Python
- The Zen of Python `import this`
- 2 or 3 ?
- RECL or IDE ?

## 数据类型
> computer是“她”
### 数
- `id()` `type()`
- round四舍五入
- `dir(math)` `help(math)`
``` python
from __future__ import division
10//3 # 3
```

### 字
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
```
- 基本操作
    * `len()`
    * `in`
    * `max` `min`
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