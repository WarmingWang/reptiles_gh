#D:\Python\Python35\python
# -*- coding:utf-8 -*-
'python课程实例：爬取大学列表'


import requests,bs4,csv,os
from bs4 import BeautifulSoup


def getHTMLText(url):
    try:
        r=requests.get(url)
        r.raise_for_status()
        r.encoding=r.apparent_encoding

        return r.text
    except:
        print('get HTML ERROR')

def fillUnivList(ulist,html):
    soup=BeautifulSoup(html,'html.parser')
    for tr in soup.find('tbody').children:
        if isinstance(tr, bs4.element.Tag):
            tds=tr('td')
            ulist.append([tds[0].string,tds[1].string,tds[2].string,tds[3].string])


def printUnivlist(ulist,num):
    tplt='{0:^10}\t{1:{4}^10}\t{2:^10}\t{3:^10}'
    print(tplt.format('排名','学校名称','省市','总分',chr(12288)))
    for i in range(num):
        u=ulist[i]
        print(tplt.format(u[0],u[1],u[2],u[3],chr(12288)))

def writeToCSV(ulist,num):
    file=open(os.path.join(os.getcwd(),'univList.csv'),'w',newline='')
    writer=csv.writer(file)
    writer.writerow(['排名','学校名称','省市','总分'])
    for i in range(num):
        u=ulist[i]
        writer.writerow([u[0],u[1],u[2],u[3]])
    file.close()

def main():
    url = 'http://www.zuihaodaxue.cn/zuihaodaxuepaiming2016.html'
    uinfo=[]
    html=getHTMLText(url)

    fillUnivList(uinfo,html)
    printUnivlist(uinfo,20) # 20 univs
    writeToCSV(uinfo,100)


main()

