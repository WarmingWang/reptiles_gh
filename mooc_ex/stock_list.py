#D:\Python\Python35\python.exe
# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
import re,traceback,os,csv
from multiprocessing import Process

def getHTMLText(url):
    try:
        r=requests.get(url,timeout=16)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
    except:
        print('获取页面异常:'+url)

def getStockList(lst,stockURL):
    html=getHTMLText(stockURL)
    sh_list=re.findall(r'<li><a target="_blank" href="http://quote.eastmoney.com/(sh[\d]{6}).html">(.*?)\([\d]*\)</a></li>',html)
    sz_list=re.findall(r'<li><a target="_blank" href="http://quote.eastmoney.com/(sz[\d]{6}).html">(.*?)\([\d]*\)</a></li>',html)
    lst.extend(sh_list)
    lst.extend(sz_list)

def getStockInfo(lst,stockURL,fpath):

    fieldnames = ['股票名称','股票代码','今开', '成交量', '最高', '涨停', '内盘', '成交额', '委比', '流通市值', '市盈率MRQ', '每股收益', '总股本', '昨收', '换手率', '最低', '跌停', '外盘', '振幅', '量比', '总市值', '市净率', '每股净资产', '流通股本']
    f_path = os.path.join(os.getcwd(), 'stockInfo.csv')
    csv_file=open(f_path,'w',newline='')
    writer=csv.DictWriter(csv_file,fieldnames=fieldnames)
    writer.writeheader()

    for count in range(600,800):
        stock=lst[count]
        print(count)

        newURL=stockURL + stock[0] + '.html'
        html=getHTMLText(newURL)

        # if not '雾霾太大' in html:
        #     pass
        # else:
        #     pass
        try:
            if html=='' or '雾霾太大' in html:
                continue
            infoDict={}

            soup=BeautifulSoup(html,'html.parser')
            stockInfo=soup.find('div',attrs={'class':'stock-bets'})
            name=stockInfo.find_all(attrs={'class':'bets-name'})[0]
            infoDict.update({'股票名称':stock[1],'股票代码':stock[0]})
            keylist=stockInfo.find_all('dt')
            valuelist=stockInfo.find_all('dd')

            for i in range(len(keylist)):
                key=keylist[i].text
                val = valuelist[i].text

                if  key in fieldnames:
                    infoDict[key]=val

            writer.writerow(infoDict)

        except:
            traceback.print_exc()
            continue

    csv_file.close()


def write2csv(item,path=os.path.join(os.getcwd(),'stockInfo.csv')):
    #传入一个列表，写到csv的一行中
    csv_file=open(path,'a+',newline='')
    writer=csv.writer(csv_file)
    writer.writerow(item)
    csv_file.close()


def main():
    stock_list_url='http://quote.eastmoney.com/stocklist.html'
    stock_info_url='https://gupiao.baidu.com/stock/'
    output_file=os.path.join(os.getcwd(),'BaidustockInfo.csv')
    slist=[]
    getStockList(slist,stock_list_url)    #list内容[('sh166105', '信达增利'), ('sh201000', 'R003'),]
    getStockInfo(slist,stock_info_url,output_file)


main()

