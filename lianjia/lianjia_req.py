# coding: utf-8

import requests,time,os,csv,re,logging
from bs4 import BeautifulSoup
import numpy as np
import traceback
from multiprocessing import Pool

def get_html(url):
    try:
        r=requests.get(url,timeout=16)
        status=r.status_code
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
    except:
        now_time=time.strftime('%Y%m%d%H%M%S')
        logging.info(now_time +'      ' +'get_html 异常, ' '    url：'+ url)


def get_n_times(page_url, n=5):
    # 获取页面失败或服务器错误是，重试n次
    i = 1
    sleep_time = 0.1
    index_page = get_html(page_url)

    while index_page == None or "小差" in index_page:
        if i > n:
            break
        else:
            time.sleep(sleep_time)
            index_page = get_html(page_url)
            sleep_time += 0.2
            i += 1
    return index_page


def get_total_page(tag_url):
    page_url = tag_url + 'd1'
    index_page = get_n_times(page_url)

    if index_page == None or "小差" in index_page:
        total_page = 101
    else:
        soup = BeautifulSoup(index_page, 'html.parser')
        taged_total_num = soup.find('div', attrs={'class': 'search-result'}).span.string
        total_page = int(taged_total_num) // 30 + 1
        if total_page > 100:
            total_page = 100
    return total_page


def parse_index_page(date, index_page, tag, page_num, total_page):
    path = os.path.join(os.getcwd(), 'results/%s_index_info_all.csv') % date  # L2：两室，P21:200万以下
    fieldnames = ['date', 'tag', 'taged_total_num', 'total_page', 'page_num', 'on_sale_num', 'saled_in_90d',
                  'last_day_viewed',
                  'key', 'title', 'total_price', 'total_price_unit', 'per_price', 'per_price_unit', 'prop1']
    if not os.path.exists(path):  # 如果文件不存在，创建文件并写入表头
        csv_file = open(path, 'w', newline='')
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        csv_file.close()

    csv_file = open(path, 'a+', newline='')
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    item = {}

    soup = BeautifulSoup(index_page, 'html.parser')

    # get_basic_info

    taged_total_num = soup.find('div', attrs={'class': 'search-result'}).span.string
    strong_num = soup.find_all('span', attrs={'class': 'num strong-num'})
    on_sale_num = strong_num[0].string  # 在售总数
    saled_in_90d = strong_num[1].string  # 近90天成交
    last_day_viewed = strong_num[2].string  # 昨天带看次数

    # update_basic_info
    item.update(
        {'date': date, 'tag': tag, 'taged_total_num': taged_total_num, 'total_page': total_page, 'page_num': page_num,
         'on_sale_num': on_sale_num, 'saled_in_90d': saled_in_90d,
         'last_day_viewed': last_day_viewed})

    index_info = soup.find_all('a', attrs={'class': 'text link-hover-green js_triggerGray js_fanglist_title'})
    for a in index_info:
        key = a['key']
        title = a['title']
        item.update({'key': key, 'title': title})

        price_div = a.parent.next_sibling.next_sibling
        total_price = price_div.find('span', attrs={'class': 'total-price strong-num'}).string
        total_price_unit = price_div.find('span', attrs={'class': 'unit'}).string
        per_price_info = price_div.find('span', attrs={'class': 'info-col price-item minor'}).string
        per_price_info = re.search('(\d+)(\S{3})', per_price_info).groups()
        per_price = per_price_info[0]
        per_price_unit = per_price_info[1]

        prop_div = price_div.next_sibling.next_sibling
        props = prop_div.find_all('span', attrs={'class': 'c-prop-tag2'})

        if len(props) > 0:
            if "距离" in props[0].string:
                prop1 = props[0].string
            else:
                prop1 = ""
        else:
            prop1 = ""

        # prop2=props[1].string
        #         prop3=props[2].string

        item.update({'total_price': total_price, 'total_price_unit': total_price_unit, 'per_price': per_price,
                     'per_price_unit': per_price_unit, 'prop1': prop1})

        writer.writerow(item)  # 定义writer2csv函数，每次调用函数写入item,结果是重复写入最后一个item，改用writer写入，无问题

    csv_file.close()


def get_page_info(date, tag, page_num, total_page, error_list=[]):
    now_time = time.strftime('%Y%m%d%H%M%S')
    page_url = base_url + tag + 'd' + str(page_num)

    index_page = get_n_times(page_url)

    if index_page != None:
        try:
            parse_index_page(date, index_page, tag, page_num, total_page)
        except:
            error_list.append(tag + 't' + str(total_page) + 'd' + str(page_num))
            logging.info(now_time + '   ' + 'Parse Error：' + tag + '  ' + str(total_page) + '  ' + 'd' + str(page_num))
            exit()

    else:
        error_list.append(tag + 't' + str(total_page) + 'd' + str(page_num))
        logging.info(now_time + '   ' + 'get None：' + tag + '  ' + str(total_page) + '  ' + 'd' + str(page_num))

    return error_list


base_url='http://sh.lianjia.com/ershoufang/'
date=time.strftime('%Y%m%d')

log_dir=os.path.join(os.getcwd(),'results/get_index.log')
logging.basicConfig(filename=log_dir,level=logging.INFO)

# filter_tag=['p21l1','p21l2','p21l3','p21l4','p21l6']
# p_tag=['p22','p23','p24','p25','p26','p27']
# l_tag=['l1','l2','l3','l4','l5','l6']
# for p in p_tag:
#     for l in l_tag:
#         filter_tag.append(p+l)

filter_tag=['p21l1']

error_list=[]
error_tag=[]

start_tag='p21l1'
start_index=filter_tag.index(start_tag)
start_page=1
sleep_time=0.2

tick = time.time()
for tag_i in range(start_index, len(filter_tag)):
    tag = filter_tag[tag_i]
    tag_url = base_url + tag
    total_page = get_total_page(tag_url)

    if total_page == 101:
        error_tag.append(tag)
        print('Tag Error: ' + str(len(error_tag)))
        continue

    if start_tag != tag:
        start_page = 1

    for page_num in range(start_page, total_page + 1):
        get_page_info(date, tag, page_num, total_page, error_list)

    print(tag + ' done, Page Error:' + str(len(error_list)))
tock = time.time()
time_cost = (tock - tick) / 60
time_cost = "%.2f" % time_cost
print('time cost: %.2f min' % ((tock - tick) / 60))  # ”%((tock-tick)/60)“需在print函数内部，否则出错

# while len(error_tag) > 0:
#     old_error_tag = error_tag
#     error_tag = []
#
#     for tag in old_error_tag:
#         tag_url = base_url + tag
#         total_page = get_total_page(tag_url)
#
#         if total_page == 101:
#             error_tag.append(tag)
#             continue
#
#         for page_num in range(1, total_page + 1):
#             get_page_info(date, tag, page_num, total_page, error_list)
#     print("number or error tag:" + str(len(error_tag)))

# while len(error_list)>0:
#     old_error_list=error_list
#     error_list=[]
#     for item in old_error_list:
#         tag=item[:5]   #返回：p21l2
#         total_page=re.search('t\d*',item).group()[1:]     #返回：纯数字
#         page_num=re.search('d\d*',item).group()[1:]       #返回：纯数字
#         get_page_info(date,tag,page_num,total_page,error_list)
#     print('number of error page: '+str(len(error_list)))

