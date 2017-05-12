# -*- coding:utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
import matplotlib
import pandas as pd

matplotlib.rcParams['font.family']='SimHei'
matplotlib.rcParams['font.size']=10

def pd_test():
    # d=pd.Series({'a':9,'b':8,'c':11})
    # d.name='Series test object'
    # d.index.name='Series index test name'
    # user=d.index.name
    # print(d,user)
    dt={
        'one':pd.Series([1,2,3],index=['a','b','c']),
        'two':pd.Series([9,8,7,6],['a','b','c','d'])
    }
    dl={
        '城市':['北京','上海','广州','深圳','沈阳'],
        '环比':[101.5,101.2,101.3,102.0,100.1],
        '同比':[120.7,127.3,119.4,140.9,101.4],
        '定基':[121.4,127.8,120.8,145.5,101.6]
    }

    d=pd.DataFrame(dl,index=['r1','r2','r3','r4','r5'])

    print(d)





pd_test()
