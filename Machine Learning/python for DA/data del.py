# -*- coding:utf-8 -*-

import pandas as pd

data=pd.read_table('DATA\mine\cav20170608_133521_1.TXT')
print(data['B室低压测量(MPa G)'][100:1000])
