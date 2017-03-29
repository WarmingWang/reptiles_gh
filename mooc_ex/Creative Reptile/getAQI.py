#D:\Python\Python35\python
# -*- coding:utf-8 -*-

import requests,os,time,re,csv
from bs4 import BeautifulSoup

def robots_test(url):
    robots_url=url + 'robots.text'
    r=requests.get(robots_url)
    if r.status_code==404:
        return True
    else:
        return False

def get_HTMLText(url):
    try:
        r=requests.get(url)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
    except:
        print("获取页面异常")

def main():
    base_url='http://aqicn.org/'
    if robots_test(base_url):
        start_url='http://aqicn.org/map/cn/'
        print(get_HTMLText(start_url))
    else:
        print('Robots协议不可')

main()

