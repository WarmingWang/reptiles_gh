#D:\Python\Python35\python.exe
# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
import re,traceback,os

def getHTMLText(url):
    pass

def getStockList(lst,stockURL):
    pass

def getStockInfo(lst,stockURL,fpath):
    pass

def main():
    stock_list_url='http://quote.eastmoney.com/stocklist.html'
    stock_info_url='https://gupiao.baidu.com/stock/'
    output_file=os.path.join(os.getcwd(),'BaidustockInfo.txt')
    slist=[]
    getStockList(slist,stock_list_url)
    getStockInfo(slist,stock_info_url,output_file)