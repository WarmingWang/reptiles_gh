# -*- coding:utf-8 -*-

import tkinter.filedialog as tk

import csv

filename=tk.askopenfilename()
csvfile=open(filename,encoding='CP932')
newname=filename.replace('秒','秒 new')
newfile=open(newname,'w',newline='\n',encoding='GBK')  #encoding='GBK'
#Y:\技术部\技术一科文件夹\金锐\NS12\R2\5.26\暖房中间\2017年05月26日 13時33分25秒.csv

reader=csv.reader(csvfile)
writer=csv.writer(newfile)

for line in reader:
    writer.writerow(line)

csvfile.close()
newfile.close()

