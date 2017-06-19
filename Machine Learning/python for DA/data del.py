# -*- coding:utf-8 -*-

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

matplotlib.rcParams['font.family']='SimHei'
matplotlib.rcParams['font.size']=10

data=pd.read_table('DATA\mine\cav20170608_133521_1.TXT')
# data.insert(0,'seconds',2)
capacity=data['试件总能力(W)'][500:8600]
capacity.plot(kind='line')

# data.plot(x=data.index,y='试件总能力(W)',kind='line')
plt.show()
