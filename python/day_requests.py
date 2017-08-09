import requests

############################# GET请求 ####################################
r = requests.get('https://unsplash.com') #get请求 返回一个response
print(r.text)
print(type(r))

loadParams = {"key1":"value1",'kay2':'value2'}
r1 = requests.get("http://httpbin.org/get", params=loadParams)

'''
<html>
...
</html>

<class 'requests.models.Response'>

实际构成了 http://httpbin.org/get?key1=value1&key2=value2
'''
############################# POST请求 ####################################

#无参数
response1 = requests.post("http://httpbin.org/post")

#有参数
payload = {'key1': 'value1', 'key2': 'value2'}
r3 = requests.post("http://httpbin.org/post", data=payload)

