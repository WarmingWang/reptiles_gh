# -*- coding:utf-8 -*-

import requests
from bs4 import BeautifulSoup

url_base='http://sh.lianjia.com/ershoufang/d'

def get_html(url):
    try:
        r=requests.get(url,timeout=16)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
    except:
        print("索引页面获取异常")

def parse_index_page(html):
    fieldnames=['title','type','area','']
    soup=BeautifulSoup(html,'html.parser')
    index_info=soup.find_all('a',attrs={'class':'text link-hover-green js_triggerGray js_fanglist_title'})
    return index_info



def parse_detail_page(detail_page):
    pass


def main():
    url=url_base + "1"
    index_page=get_html(url)
    info=parse_index_page(index_page)



main()

