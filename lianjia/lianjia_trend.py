
# coding: utf-8

import requests,time,os,csv,re,logging
from bs4 import BeautifulSoup
import numpy as np
import traceback

from lianjia_requests import get_n_times


ex_date = time.strftime('%Y%m%d')
ex_time = time.strftime('%H:%M:%S')

print(ex_date + "_" + ex_time+ " 正在获取..." + "\n")

url = 'http://sh.lianjia.com/ershoufang'
html =get_n_times(url, n=6)

soup=BeautifulSoup(html,'html.parser')
spans=soup.find_all('span',attrs={'class':'num strong-num'})

total_on_sale=spans[0].string
last_90day_deal = spans[1].string
yesterday_viewed = spans[2].string

item={'ex_date':ex_date,
      'ex_time':ex_time, 
      'total_on_sale':total_on_sale,
      'last_90day_deal':last_90day_deal,
      'yesterday_viewed':yesterday_viewed}

path=os.path.join(os.getcwd(),'results/lianjia_trends.csv')

fieldnames=['ex_date','ex_time', 'total_on_sale','last_90day_deal', 'yesterday_viewed']

if  not os.path.exists(path):     #如果文件不存在，创建文件并写入表头
        csv_file=open(path,'w',newline='')
        writer=csv.DictWriter(csv_file,fieldnames=fieldnames)
        writer.writeheader()
        csv_file.close()
        
csv_file=open(path,'a+',newline='')
writer=csv.DictWriter(csv_file,fieldnames=fieldnames)
writer.writerow(item)
csv_file.close()


n=3
print('获取结束，%d秒后关闭' %n)  
time.sleep(n)

