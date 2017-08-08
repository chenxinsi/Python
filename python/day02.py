#####################将Unicode文本统一表示为规范形式############################

s1 = 'Spicy Jalape\u00f1o'
s2 = 'Spicy Jalapen\u0303o'
print(s1)
print(s2)

'''
Spicy Jalapeño
Spicy Jalapeño
'''

print(s1==s2)
print('s1:',len(s1))
print('s2:',len(s2))

'''
False
s1: 14
s2: 15
'''

'''
同一文本拥有多种不同的表示形式是个大问题，
应该先将文本统一表示为规范形式
可以通过 unicodedata模块
'''

import unicodedata

t1 = unicodedata.normalize('NFC', s1)
t2 = unicodedata.normalize('NFC', s2)
print(t1 == t2)
print('t1:',ascii(t1),'t2:',ascii(t2))

t3 = unicodedata.normalize('NFD', s1)
t4 = unicodedata.normalize('NFD', s2)
print(t3 == t4)
print('t3:',ascii(t3),'t4:',ascii(t4))

'''
True
t1: 'Spicy Jalape\xf1o' t2: 'Spicy Jalape\xf1o'
True
t3: 'Spicy Jalapen\u0303o' t4: 'Spicy Jalapen\u0303o'


NFC: 字符全组成
NFD: 组合字符
'''
t5 = '\ufb01'
str1 = unicodedata.normalize('NFD', t5)
print(str1,':',ascii(str1))

str2 = unicodedata.normalize('NFKD', t5)
str3 = unicodedata.normalize('NFKC', t5)
print(str2, ":", ascii(str2))
print(str3, ":", ascii(str3))
'''
ﬁ : '\ufb01'
fi : 'fi'
fi : 'fi'
'''

####################################用正则表达式处理Unicode字符############################################
