#!/usr/local/bin/python3

import requests

'''
 username=13521423540&password=r63336180&captcha=&style=1&third_parts=111&other_parts=111&forms=11&login_type=2&history=aHR0cDovL2h1aGVoYW90ZS5hbmp1a2UuY29tLw%3D%3D&token=ODMzOWJkNjZjYTMwMDI2MmIxYjE1ODU1NDRmYTFhNmY%3D&token2=325d9225600faf6c1d760d2bcf2dceecf3326eb0f26a370c25289efa971f050b
'''
# r = requests.post("http://www.0478xinxi.com", data={"username" : "13521423540", "password" : "r63336180", "captcha" : "", "style" : 1, "third_parts" : 111, "other_parts" : 111, "forms" : 11, "login_type" : 2, "history" : "aHR0cDovL2h1aGVoYW90ZS5hbmp1a2UuY29tLw%3D%3D", "token" : "ODMzOWJkNjZjYTMwMDI2MmIxYjE1ODU1NDRmYTFhNmY%3D", "token2" : "325d9225600faf6c1d760d2bcf2dceecf3326eb0f26a370c25289efa971f050b"})

#print(r.status_code)

# r = requests.put("http://www.test.com", data = {"title":"test"})
# r = requests.delete("http://www.test.com")
#r = requests.head("http://www.anjuke.com")

# r = requests.options("http://www.baidu.com")

# 自定义header
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36", "Cookie":'haha'}
# 发起带参数GET请求
r = requests.get("http://www.0478xinxi.com", params = {"a" : "guo", "b":"rui"}, headers = headers)
# requests 默认自动重定向， 想取消默认重定向设置 allow_redirects= False
r = requests.get("http://www.anjuke.com", allow_redirects = False)

# 设置请求超时时间, 使用timeout关键字，单位秒
r = requests.get("http://www.0478xinx.com", timeout = 3)

# 请求的url
print(r.url)
# HTTP响应状态码
print(r.status_code)
# 响应的编码方式
print(r.encoding)
# 响应的headers头信息
print(r.headers)
# 响应的cookies信息
print(r.cookies)
# 响应的主体内容
print(r.text)
