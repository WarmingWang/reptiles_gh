# -*- coding:utf-8 -*-
import json,re

import pandas as pd;import numpy as np
import matplotlib.pyplot as plt

path='data/ch02/usagov_bitly_data2012-03-16-1331923249.txt'


records=[json.loads(line) for line in open(path)]
time_zones=[rec['tz'] for rec in records if 'tz' in rec]  #列表解析/列表推导
frame=pd.DataFrame(records)

def get_counts(sequense):
    counts={}
    for x in sequense:
        if x in counts:
            counts[x]+=1
        else:
            counts[x]=1
    return counts

def get_counts2(sequence):
    from collections import defaultdict
    counts=defaultdict(int)  #字典的values都是int类型，key不存在时value=int()的默认值0
    for x in sequence:
        counts[x]+=1     #第一次循环到key x时，count[x]返回0，执行完后，count[x]=1
    return counts

def top_counts(count_dict,n=10):

    # 字典按照key 或 value 进行排序
    new = sorted(count_dict.items(), key=lambda d: d[1], reverse=True)   #参数d是一个item()
    return new[:n]

def sort_dict(count_dict,n=10):
    dic2list=[(count,tz) for tz,count in count_dict.items()]
    dic2list.sort(reverse=True)   #改变原列表的结构，不返回任何值。 new=dic2list.sort()  →运行后new=None
    return dic2list[:n]

def countByCounter(tz_dic,n=5):
    from collections import Counter
    c=Counter(tz_dic)
    return c.most_common(n)

def countByPandas(n=10):

    frame.to_csv('out.csv')
    tz=frame['tz']
    clean_tz=tz.fillna('Missing')
    clean_tz[clean_tz=='']='unknown'   #DataFrame类型数据过滤
    tz_counts=clean_tz.value_counts()[:n]

    #Series对象直接绘图
    tz_counts.plot(kind='barh',rot=60)

    plt.show()
    print(tz_counts)

def get_browser():
    browsers=pd.Series([x.split()[0] for x in frame.a.dropna()])
    browsers_count=browsers.value_counts()[:10]
    browsers_count.plot(kind='bar',rot=45)
    plt.show()

def win_count():
    cframe=frame[frame.a.notnull()]  #DataFrame类型数据过滤/筛选http://blog.csdn.net/jt1123/article/details/50086595
    o_s=np.where(cframe['a'].str.contains('Windows'),'Windows','Not Windows')    #返回一个ndarray类型
    by_tz_os=cframe.groupby(['tz',o_s])
    agg_count=by_tz_os.size().unstack().fillna(0)
    indexer=agg_count.sum(1).argsort()  #返回数组从小到大排列后的索引值
    print(indexer)


def test():
    np.random.seed(5)
    df=pd.DataFrame({'key1':['a','a','b','b','a'],
                   'key2':['one','two','one','two','one'],
                   'data1':np.random.randn(5),
                   'data2':np.random.randn(5)})
    gp1=df.groupby(['key1','key2'])
    gp2=df.groupby([1,1,2,2,1])
    print(gp2.mean(  ))
    print(gp1.mean())


win_count()
# test()