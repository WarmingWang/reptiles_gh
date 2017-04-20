# -*- coding:utf-8 -*-
import numpy as np
# a=np.arange(100).reshape((5,10,2))
# np.savetxt('a.csv',a,fmt='%.3f',delimiter=',')

# b=np.loadtxt('a.csv',dtype=np.float ,delimiter=',')


# aa.tofile('aa.dat',sep=',', format='%.2f')

# c=np.fromfile('aa.dat',dtype=np.float,sep=',')
# np.save('a.npy',a)
na=np.load('a.npy')
print(na.shape)