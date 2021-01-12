# -*- coding:utf-8 -*-

from PIL import Image
import os 
from selenium import webdriver
import requests
import numpy as np
import time
from datetime import datetime
import pandas as pd 

time1 = time.time()
#计算png的sum值
def sum_png(png_path):
    image = Image.open(png_path)
    image_arr = np.array(image)
    return np.sum(image_arr)

#将星级图片的url转换为sum值
def url2sum(url):
    r = requests.get(url)
    with open("temp.png", "wb")as f:
        f.write(r.content)
    return sum_png('temp.png')   

#将列表中的数字文本转为float类型
def text2float(text_list):
    float_list=[]
    for item in text_list:
        try:
            item = float(item)
        except:
            pass
        float_list.append(item)
    return float_list

#将字典转化为series
def dic2series(keys,values):
    make_dic = dict(zip(keys,values))
    return pd.Series(make_dic)

#模拟登录
def login_with_firefox():
    global browser
    browser = webdriver.Firefox()

    #只加载10s
    browser.set_page_load_timeout(8)

    try:
        browser.get('https://cn.morningstar.com/quickrank/default.aspx')
    except Exception:
        time.sleep(5)
        browser.execute_script('window.stop()')

    #模拟用户登录
    username = browser.find_element_by_id('emailTxt')
    password = browser.find_element_by_id('pwdValue')

    username.send_keys('ryan_jin@sina.com')  
    password.send_keys('pa_wo@17.ms')
    submit = browser.find_element_by_id('loginGo')
    
    try:
        submit.click()
    except:
        time.sleep(3)
        try:
            submit.click()
        except:
            time.sleep(3)
            try:
                submit.click()
            except:
                return None           
    time.sleep(10)
    browser.execute_script('window.stop()')
    
def get_urls(number_of_page):
    pu_tong_gu_piao = browser.find_element_by_id('ctl00_cphMain_cblCategory_0')
    ji_ji_pei_zhi = browser.find_element_by_id('ctl00_cphMain_cblCategory_7')
    ling_huo_pei_zhi = browser.find_element_by_id('ctl00_cphMain_cblCategory_8')
    san_nian_3_xing = browser.find_element_by_id('ctl00_cphMain_cblStarRating_0')
    wu_nian_3_xing = browser.find_element_by_id('ctl00_cphMain_cblStarRating5_0')
    kai_fang_shi = browser.find_element_by_id('ctl00_cphMain_cblGroup_0')
    search = browser.find_element_by_id('ctl00_cphMain_btnGo')

    try:
        pu_tong_gu_piao.click()
        ji_ji_pei_zhi.click()
        ling_huo_pei_zhi.click()
        san_nian_3_xing.click()
        wu_nian_3_xing.click()
        kai_fang_shi.click()
        search.click()
        time.sleep(5)
    except Exception:
        browser.execute_script('window.stop()')

    urls_auto_get=[]
    for i in range(1,number_of_page+1):
        table = browser.find_element_by_id('ctl00_cphMain_gridResult')
        tds = table.find_elements_by_tag_name('a')
        a_hrefs_du = [tds[i].get_attribute('href') for i in range(len(tds))]
        
        #去重，并保持原来的顺序
        a_hrefs=[]
        for item in a_hrefs_du:
            if item not in a_hrefs:
                a_hrefs.append(item)
        
        # a_hrefs = list(set(a_hrefs))   #去重，但是顺序会变得随机
        
        for item in a_hrefs:
            if item.find('java') < 0:
                urls_auto_get.append(item)
        if i <= number_of_page-1:
            try:
                next_page = browser.find_element_by_link_text('>')
                next_page.click()
            except Exception:
                browser.execute_script('window.stop()')

    return urls_auto_get

def get_info_by_fund_url(fund_url):
    try:
        browser.get(fund_url)
    except Exception:
        browser.execute_script('window.stop()')

    qt_base = browser.find_element_by_id('qt_base')

    #基金代码 & 名称
    f_title = browser.find_element_by_id('qt_fund').text
    f_code =f_title[:6]
    f_name = f_title[7:]

    #净值
    jingZhi = float(qt_base.find_element_by_xpath('//div/ul/li[2]/span').text)

    #净值日期
    jingZhiDate = qt_base.find_element_by_class_name('date').text[5:]

    #基金类型
    f_type = qt_base.find_element_by_class_name('category').text

    #创建时间
    found_date = qt_base.find_element_by_class_name('inception').text

    #基金风格箱
    f_style = qt_base.find_element_by_class_name('sbdesc').text

    #总净资产（亿元）
    total_asset = float(qt_base.find_element_by_class_name('asset').text)

    #基金管理信息[基金公司，基金经理，接手时间，任职时间]
    qt_management = browser.find_element_by_id('qt_management')
    #基金公司名称
    company_name = qt_management.find_elements_by_tag_name('a')[1].text

    qt_manager = browser.find_element_by_id('qt_manager')
    #基金经理
    f_manager = qt_manager.find_elements_by_tag_name('a')[0].text
    #接手时间
    manager_from = qt_manager.find_elements_by_tag_name('i')[0].text[:10]
    #任职时间
    manager_time = qt_manager.find_elements_by_tag_name('span')[0].text[5:]

    # manage_info_keys = ['基金公司名称','基金经理','接手时间','任职时间']
    # manage_info_values = [company_name,f_manager,manager_from,manager_time]
    # manage_info = dict(zip(manage_info_keys,manage_info_values))
    # manage_info_series = pd.Series(manage_info)
    
    #[基金代码，名称，基金公司，基金经理，接手时间，任职时间,基金类型，基金风格箱，总净资产,净值，净值日期，创建时间，]
    base_info_values = text2float([f_code,f_name,company_name,f_manager,manager_from,manager_time,
                                    f_type,f_style,total_asset,jingZhi,jingZhiDate,found_date])
    base_info_keys = ['代码','名称','基金公司','基金经理','接手时间','任职时间','分类','风格','总净资产(亿元)','净值','净值日期','创建时间']
    base_info =dict(zip(base_info_keys,base_info_values))
    base_info_series  = pd.Series(base_info)
    

    #获取近8年的业绩表现
    qt_per = browser.find_element_by_id('qt_per')
    performance_8_values =text2float([qt_per.find_element_by_class_name(r_x).text 
                                      for r_x in ['r0','r1','r2','r3','r4','r5','r6','r7']])

    this_year = datetime.now().year

    performance_8_keys = ['今年业绩%',
                          str(this_year-1 ) + "业绩(%)" ,
                          str(this_year-2 ) + "业绩(%)" ,
                          str(this_year-3 ) + "业绩(%)" ,
                          str(this_year-4 ) + "业绩(%)" ,
                          str(this_year-5 ) + "业绩(%)" ,
                          str(this_year-6 ) + "业绩(%)" ,
                          str(this_year-7 ) + "业绩(%)" ,]

    performance_8 = dict(zip(performance_8_keys,performance_8_values))
    performance_8_series  = pd.Series(performance_8)
    
    qt_return1= browser.find_element_by_id('qt_return1')

    #历史回报[一个月，三个月，六个月，今年以来，一年，二年年化，三年年化，五年年化，十年年化]
    history_return_values = text2float([qt_return1.find_elements_by_tag_name('li')[li_no].text 
                                        for li_no in [6,11,16,21,26,31,36,41,46]])

    history_return_keys = ['一个月回报',
                          '三个月回报',
                          '六个月回报',
                          '今年回报',
                          '一年年化',
                          '两年年化',
                          '三年年化',
                          '五年年化',
                          '十年年化']
    history_return = dict(zip(history_return_keys,history_return_values))
    history_return_series = pd.Series(history_return)

    qt_worst = browser.find_element_by_id('qt_worst')

    #最差3个月，最差6个月回报
    worst3_6_values = text2float([qt_worst.find_elements_by_tag_name('li')[li_no].text for li_no in [1,3]])
    worst3_6_keys = ['最差3个月回报','最差6个月回报']
    worst3_6_series = dic2series(worst3_6_keys,worst3_6_values)

                              
    #获取评级的图片url
    qt_star =browser.find_element_by_id('qt_star')
    star_elements = qt_star.find_elements_by_tag_name('img')
    star_urls = [star_elements[no_img].get_attribute("src") for no_img in [0,1,2]]

    #计算0-5星的sum值以备查找
    stars_sum = [sum_png('0.png'),sum_png('1.png'),sum_png('2.png'),sum_png('3.png'),sum_png('4.png'),sum_png('5.png')]

    #获取本基金3年/5年/10年评级图片sum值
    these_stars = [url2sum(url) for url in star_urls]

    #比对sum值获得评级
    stars_level_values = [stars_sum.index(sum_value) for sum_value in these_stars]
    stars_level_keys = ['3年评级','5年评级','10年评级']
    stars_level_series = dic2series(stars_level_keys,stars_level_values)
                              
    qt_risk = browser.find_element_by_id('qt_risk')
    qt_risk_lists = qt_risk.find_elements_by_tag_name('li')

    #标准差，晨星风险系数，夏普比率3年，夏普比率5年，夏普比率10年
    risks1 = [qt_risk_lists[li_no].text for li_no in [15,22,29,31,33]]

    qt_riskstats =browser.find_element_by_id('qt_riskstats')
    qt_riskstats_lists = qt_riskstats.find_elements_by_tag_name('li')

    #阿尔法系数，贝塔系数，R平方
    risks2 = [qt_riskstats_lists[li_no].text for li_no in [4,7,10]]

    #risk输出
    risks_values = text2float(risks1 + risks2)
    risks_keys = ['标准差',
                 '晨星风险系数',
                 '夏普比率3年',
                 '夏普比率5年',
                 '夏普比率10年',
                 '阿尔法系数',
                 '贝塔系数',
                 'R平方']
    risks_series = dic2series(risks_keys,risks_values)    
                              
    qt_rating = browser.find_element_by_id('qt_rating')

    #获取src字符串的星级数字
    these_rating_stars = [qt_rating.find_elements_by_tag_name('img')[li_no].get_attribute("src")[-10] for li_no in [0,1,2,3]]
    risk_stars_values = text2float(these_rating_stars)
    risk_stars_keys = ['2年风险',
                        '3年风险',
                        '5年风险',
                        '10年风险']
    risk_stars_seriis = dic2series(risk_stars_keys,risk_stars_values)  
                              
    qt_asset = browser.find_element_by_id('qt_asset')

    cash_pencent = qt_asset.find_element_by_class_name('cash').text
    stock_pencent = qt_asset.find_element_by_class_name('stock').text
    bonds_pencent = qt_asset.find_element_by_class_name('bonds').text

    #【现金，股票，债券】
    asset_distribution_values = text2float([cash_pencent,stock_pencent,bonds_pencent])
    asset_distribution_keys = ['现金比例(%)',
                              '股票比例(%)',
                              '债券比例(%)']
    asset_distribution_series = dic2series(asset_distribution_keys,asset_distribution_values)

    info_sorted_keys= ['基金经理','夏普比率3年','夏普比率5年','夏普比率10年','晨星3年','晨星5年','晨星10年']
    info_sorted_values = [f_manager,risks1[2],risks1[3],risks1[4]] + stars_level_values
    info_sorted_series = dic2series(info_sorted_keys,info_sorted_values)
                              
    data_series = pd.concat([base_info_series,
                             performance_8_series,
                             history_return_series,
                             worst3_6_series,
                             stars_level_series,
                             risks_series,
                             risk_stars_seriis,
                             asset_distribution_series,
                             info_sorted_series])
    
    return data_series 

def get_info_ss(n_page,n_funds,self_urls):
    n_funds = n_funds + len(self_urls)
    urls =  self_urls + get_urls(n_page)
    ss =[]
    i = 0
    for fund_url in urls:
        try:
            ss_one = get_info_by_fund_url(fund_url)
            ss.append(ss_one)
        except Exception:
            time.sleep(3)
            try:
                ss_one = get_info_by_fund_url(fund_url)
                ss.append(ss_one)
            except Exception:
                time.sleep(3) 
                try:
                    ss_one = get_info_by_fund_url(fund_url)
                    ss.append(ss_one) 
                except Exception:
                    pass
        i = i+1
        if i >n_funds:
            break
    # ss = [get_info_by_fund_url(fund_url) for fund_url in urls]   
    browser.quit()
    return urls,ss

def get_ids(urls):
    fund_ids=[]
    for item in urls:
        id = item[-10:]
        fund_ids.append(id)
    return fund_ids

login_with_firefox()

#输入自定义基金的url,排行榜的页面，排行榜的前n位基金
self_urls=['https://cn.morningstar.com/quicktake/F0000003YD',
           'https://cn.morningstar.com/quicktake/0P00016JIH',
           'https://cn.morningstar.com/quicktake/F0000004JE']
urls,ss = get_info_ss(10,200,self_urls)


fund_ids = get_ids(urls)
df = pd.DataFrame(dict(zip(fund_ids,ss)))
df = pd.DataFrame(df.values.T, index=df.columns, columns=df.index)

now_time=datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
csv_path = now_time + '.csv'
df.to_csv(csv_path, sep=',', header=True, index=True,encoding='utf_8_sig')

time2 = time.time()
print("用时:" + str(round((time2-time1)/60,2)) + "min")