# -*- coding:utf-8 -*-

import numpy as np

from sklearn.cluster import KMeans

if __name__=='__main__':
    data=np.genfromtxt('city.txt',delimiter=',')