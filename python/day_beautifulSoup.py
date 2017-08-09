'''
Beautiful Soup将复杂HTML文档转换成一个复杂的树形结构
每个节点都是Python对象。
所有对象可以归纳为4种类型:Tag , NavigableString , BeautifulSoup , Comment 。
'''
import bs4
from bs4 import BeautifulSoup

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">123</p>
"""

soup = BeautifulSoup(html_doc,'lxml')
find = soup.find('p')
print("results type is:",type(find))
print("results content:",find)
print("find name: ",find.name)
print("class is : ", find['class'])

findAll = soup.find_all('p')
print(findAll)
for item in findAll:
    print(item.string,"\n")

'''
用find方法找寻第一个<p>标签
results type is: <class 'bs4.element.Tag'>
results content: <p class="title"><b>The Dormouse's story</b></p>
find name:  p
class is :  ['title']
'''

markup = "<b><!--Hey buddy Want to buy a used parser?--></br>"
soup1 = BeautifulSoup(markup,'lxml')
comment = soup1.b.string
print(comment)

if type(comment) == bs4.element.Comment:
    print('该字符是注释')
else:
    print('该字符不是注释',type(comment))

for child in soup.children:
    print(child)

for parent in soup.parents:
    if parent is None:
        print(parent)
    else:
        print(parent.name)

print(soup.find_all("title"))
print(soup.find_all("p","title"))
print(soup.find_all("a"))