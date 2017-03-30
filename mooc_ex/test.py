#D:\Python\Python35\python.exe
# -*- coding:utf-8 -*-

import csv,requests
from bs4 import BeautifulSoup
f_path=r'C:\users\acer\desktop\test.csv'
import re

str='成都  (72)'
s=re.search(r'(.*?)  \((\d+)\)',str)
print(s.groups())