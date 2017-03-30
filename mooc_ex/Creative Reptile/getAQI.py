#D:\Python\Python35\python
# -*- coding:utf-8 -*-

import requests,re,csv,traceback,os,time
from bs4 import BeautifulSoup

start_time=time.strftime("%Y%m%d_%H%M%S", time.localtime())
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

def get_cityDict(cityDict,html):
    soup = BeautifulSoup(html, 'html.parser')
    china_aTag = soup.find('a', attrs={'href': r'http://aqicn.org/map/china/cn/'})
    china = china_aTag.parent
    cities = china.find_all('a')
    for i in range(1,len(cities)):
        name=cities[i].text
        url=cities[i].attrs['href']
        cityDict[name]=url

def getStationAQI(city_name, city_url):
    aqi=[]
    html=get_HTMLText(city_url)
    soup=BeautifulSoup(html,'html.parser')
    try:
        target=soup.find('div',attrs={'class':'map-stations max-height max-height-300'})
        get_time=time.strftime("%Y%m%d_%H%M%S", time.localtime())
        aqi.append([city_name+'(爬取时间：'+str(get_time)+')'])
        stationTags=target.find_all('a')
        for i in range(len(stationTags)):
            content=stationTags[i].text
            re_split=re.search(r'(.*?)  \((\d+)\)',content)
            station_name=re_split.group(1)
            station_aqi=re_split.group(2)
            aqi.append(['',station_name,station_aqi])
        return aqi
    except:
        # traceback.print_exc()
        pass

def write2csv(list):
    csv_header=['省份/城市','站点名称','空气质量指数']
    path=os.path.join(os.getcwd(),str(start_time) + '.csv')

    not_exsits=False
    if not os.path.exists(path):        not_exsits=True  #判断文件是否存才并保存状态

    csv_file=open(path,'a',newline='')
    writer=csv.writer(csv_file)

    if not_exsits:
        writer.writerow(csv_header)

    try:
        for item in list:
            writer.writerow(item)
    except:
        # traceback.print_exc()
        pass

    csv_file.close()

def main():
    base_url='http://aqicn.org/'
    if robots_test(base_url):
        start_url='http://aqicn.org/map/cn/'
        html=get_HTMLText(start_url)
        cityDict={}
        get_cityDict(cityDict,html)

        for city_name, city_url in cityDict.items():
            aqilist=getStationAQI(city_name, city_url)
            write2csv(aqilist)

    else:
        print('Robots协议不可')

main()
# testDict={'成都': 'http://aqicn.org/map/chengdu/cn/', }
# for city_name, city_url in testDict.items():
#     aqilist=getStationAQI(city_name, city_url)
#     write2csv(aqilist)


