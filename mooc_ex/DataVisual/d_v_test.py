# -*- coding:utf-8 -*-
import numpy as np
from PIL import Image

# a=np.arange(100).reshape((5,10,2))
# np.savetxt('a.csv',a,fmt='%.3f',delimiter=',')

# b=np.loadtxt('a.csv',dtype=np.float ,delimiter=',')


# aa.tofile('aa.dat',sep=',', format='%.2f')

# c=np.fromfile('aa.dat',dtype=np.float,sep=',')
# np.save('a.npy',a)
im=np.array(Image.open(r"F:\pyc\PyCharm\GitHub\reptiles_gh\mooc_ex\DataVisual\sea.jpg"))
b=[255,255,255]-im
bw_im=  Image.fromarray(b.astype(('uint8')))
bw_im.save(r'F:\pyc\PyCharm\GitHub\reptiles_gh\mooc_ex\DataVisual\bw_sea.jpg')