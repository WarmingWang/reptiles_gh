#D:\Python\Python35\python.exe
# -*- coding:utf-8 -*-
'淘宝商品价格定向爬虫'

import requests,csv,re,os,time

def getHTMLtext(url):
    try:
        r=requests.get(url)
        r.encoding=r.apparent_encoding
        return r.text
    except:
        print('获取页面异常')

def parsePage(ilt,html):
    info=re.findall(r'raw_title":"(.*?)",.*?,"view_price":"(.*?)".*?"view_sales":"(.*?)","comment_count":"(.*?)"',html)   #
    ilt.append(info)
    # view_price=re.findall(r'"view_price":"(.*?)"',html)
    # view_sales=re.findall(r'"view_sales":"(.*?)"',html)


def write2csv(ilt,fpath):
    with open(fpath,'w+',newline='\n') as csvfile:
        writer=csv.writer(csvfile)
        for m in range(len(ilt)):
            for i in range(len(ilt[m])):
                writer.writerow(ilt[m][i])
        csvfile.close()


def main():
    kw = '书包'
    url='https://s.taobao.com/search?q='+kw
    ilt=[]
    depth=2
    csv_path=os.path.join(os.getcwd(),'xbaoItem.csv')
    for i in range(depth):
        html=getHTMLtext(url+'&s='+str(44*i))
        parsePage(ilt,html)
        print(i)
        # time.sleep(15)

    write2csv(ilt,csv_path)


if __name__=='__main__':
    main()
