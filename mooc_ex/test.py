#D:\Python\Python35\python.exe
# -*- coding:utf-8 -*-

import requests

r=requests.get('https://gupiao.baidu.com/stock/sh204003.html')
r.encoding=r.apparent_encoding
if not '雾霾太大' in r.text:
    print('you')
else:
    print('wu')
print(r.status_code)
# print(r.text)