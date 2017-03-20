#D:\Python\Python35\python
# -*- coding:utf-8 -*-

import requests,re,csv


def get_cookie():
    cookies = {}
    filePath=r'd:\cookies\weibo.com cookie.txt'
    file=open(filePath,'r')
    text=file.read()
    regx='(\w.*?)=(.*?);'
    items=re.findall(regx,text)
    for item in items:
        cookies[item[0]]=item[1]
    return cookies

cookies=get_cookie()

headers={'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0'}
url='http://weibo.com/275599406?from=myfollow_group&is_all=1'
r=requests.get(url,cookies=cookies)
r.encoding=r.apparent_encoding
print(cookies)
