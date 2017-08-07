# -*- coding:utf-8 -*-

#字符串和文本

#
#针对任意多的分隔符拆分字符串
#

#捕获组 和 非捕获组（?:...）
import re
line = 'asdf fjdk; afed, fjek,asdf,   foo'
list = re.split(r'[;,\s]\s*', line)
print (list)
#输出结果：['asdf', 'fjdk', 'afed', 'fjek', 'asdf', 'foo']


#捕获组
fields = re.split(r'(;|,|\s)\s*', line)
print (fields)
#输出结果： ['asdf', ' ', 'fjdk', ';', 'afed', ',', 'fjek', ',', 'asdf', ',', 'foo']


#非捕获组
fieldssss = re.split(r'(?:;|,|\s)\s*',line)
print (fieldssss)
#输出结果： ['asdf', 'fjdk', 'afed', 'fjek', 'asdf', 'foo']


#
#文本模式的匹配和查找
#

text1 = '2017-06-21 11:48'
text2 = '2017／01／22 11:23'

if re.match(r'\d+-\d+-\d+\s\d+:\d+', text2):
    print('yes')
else:
    print('no')
#输出结果：text1：yes text2：no

#正则表达式预编译成一个模式对象
datepat = re.compile(r'\d+-\d+-\d+')
if datepat.match(text1):
    print("yes")
else:
    print("no")
#输出结果为： yes

if datepat.match(text2):
    print("yes")
else:
    print("no")
#输出结果为： no

#match()方法总是尝试在字符串的开头找到匹配项
#如果想针对整个文本搜索出所有的匹配项，那么应该使用findall()方法
text = 'Today is 2017-01-01. PyCon starts 2012-02-02'
print(datepat.findall(text))
#输出结果为： ['2017-01-01', '2012-02-02']

#捕获组的内容可以单独提取出来
datepat1 = re.compile(r'(\d+)-(\d+)-(\d+)')
m = datepat1.match('2017-10-01')
print(m.group(0))
print(m.group(1))
print(m.group(2))
print(m.group(3))
print(m.groups())

'''
输出结果为：
2017-10-01
2017
10
01
('2017', '10', '01')
'''

###################################查找和替换文本##############################################

string = 'yeah, but no, but yeah, but no, but yeah'
print(string.replace('yeah','yep'))

#输出结果为： yep, but no, but yep, but no, but yep

