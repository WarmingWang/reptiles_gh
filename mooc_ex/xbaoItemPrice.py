#D:\Python\Python35\python.exe
# -*- coding:utf-8 -*-
'淘宝商品价格定向爬虫'

import requests,csv,re,os,time

i=1  #全局计数变量

def getHTMLtext(url):
    try:
        r=requests.get(url)
        r.encoding=r.apparent_encoding
        return r.text
    except:
        print('获取页面异常')

def parsePage(ilt,html):
    # info=re.findall(r'raw_title":"(.*?)",.*?,"view_price":"(.*?)".*?"view_sales":"(.*?)人付款","comment_count":"(.*?)"',html)   #
    # for item in info:
    #     ilt.append(list(item))
    # print(ilt)
    global i
    info=re.finditer(r'raw_title":"(.*?)",.*?,"view_price":"(.*?)".*?"view_sales":"(.*?)人付款","comment_count":"(.*?)"',html)   #

    for item in info:
        ilt.append([i,item.group(1),item.group(2),item.group(3),item.group(4)])
        i+=1


    # view_price=re.findall(r'"view_price":"(.*?)"',html)
    # view_sales=re.findall(r'"view_sales":"(.*?)"',html)


def write2csv(item,fpath):
    with open(fpath,'a+',newline='\n') as csvfile:
        writer=csv.writer(csvfile)
        # for m in range(len(ilt)):
        #     for i in range(len(ilt[m])):
        #         writer.writerow(ilt[m][i])
        writer.writerow(item)
        csvfile.close()


def main():
    kw = '收纳盒'
    url='https://s.taobao.com/search?q='+kw
    ilt=[[kw],['No.','名称','价格','付款人数','评论数']]
    page=1
    csv_path=os.path.join(os.getcwd(),'xbaoItem.csv')
    for i in range(page):
        html=getHTMLtext(url+'&s='+str(44*i))
        parsePage(ilt,html)
        time.sleep(5)
        print(i)
        for item in ilt:
            write2csv(item,csv_path)
        ilt.clear()  #降低内存占用
    # print(ilt)

if __name__=='__main__':
    main()
