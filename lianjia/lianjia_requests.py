# -*- coding:utf-8 -*-

import requests

url_base='http://sh.lianjia.com/ershoufang/d'

def get_html(url):
    try:
        r=requests.get(url,timeout=16)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
    except:
        print("索引页面获取异常")

def parse_index_page(index_page):
    pass

def parse_detail_page(detail_page):
    pass


