#D:\Python\Python35\python.exe
# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
import re,traceback,os,csv
import

def getHTMLText(url):
    try:
        r=requests.get(url)
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
    for stock in lst:
        stockURL=stockURL + stock[0] + '.html'
        html=getHTMLText(stockURL)

        # if not '雾霾太大' in html:
        #     pass
        # else:
        #     pass
        try:
            if html=='':
                continue
            infoDict={}
            soup=BeautifulSoup(html,'html.parser')
            stockInfo=soup.find('div',attrs={'class':'stock-bets'})

            name=stockInfo.find_all(attrs={'class':'stock-bets'})[0]
            infoDict.update({'股票名称':name.text.split()[0]})

            keylist=stockInfo.find_all('dt')
            valuelist=stockInfo.find_all('dd')
            for i in range(len(keylist)):
                key=keylist[i].text
                val=valuelist[i].text
                infoDict[key]=val

            #以字典形式写入CSV


        except:
            traceback.print_exc()
            continue



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
    print(slist)


main()

