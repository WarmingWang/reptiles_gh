# -*- coding:utf-8 -*-

import pandas as pd

data=pd.read_table('DATA\mine\cav20170608_133521_1.TXT')
data.insert(0,'seconds',2)

print(data[:3].icol[:1])
