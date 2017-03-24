#D:\Python\Python35\python.exe
# -*- coding:utf-8 -*-

import csv,requests
from bs4 import BeautifulSoup
f_path=r'C:\users\acer\desktop\test.csv'

url='https://gupiao.baidu.com/stock/sh600050.html'
r=requests.get(url)
r.encoding=r.apparent_encoding
print(r.status_code)
html=r.text
soup=BeautifulSoup(html,'html.parser')
stockInfo=soup.find('div',attrs={'class':'stock-bets'})
infoDict={}
name=stockInfo.find_all(attrs={'class':'bets-name'})[0]
infoDict.update({'股票名称':name.text.split()[0]})
fieldnames=[]
keylist=stockInfo.find_all('dt')
valuelist=stockInfo.find_all('dd')
for i in range(len(keylist)):
    key=keylist[i].text
    fieldnames.append(key)
print(fieldnames)
