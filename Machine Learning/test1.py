# -*- coding:utf-8 -*-

import matplotlib.pyplot as plt
from sklearn import datasets
import seaborn as sns
# import csv

from sklearn import decomposition
from sklearn import manifold
from matplotlib.ticker import NullFormatter
from time import time


def write2csv(item):
    pass

n_componets=2
n_neighbors=10

data=datasets.load_iris()
x=data.data
color=data.target

fig=plt.figure(figsize=(15,4))

t0=time()
Y=manifold.Isomap(n_neighbors,n_componets).fit_transform(x)
t1=time()
print('Isomap: %2g sec' %(t1-t0))
ax=fig.add_subplot(151)
plt.scatter(Y[:,0],Y[:,1],c=color,cmap=plt.cm.Set1)
plt.title('Isomap (%.2g sec' %(t1-t0))
ax.xaxis.set_major_formatter(NullFormatter())
ax.yaxis.set_major_formatter(NullFormatter())
plt.axis("tight")

plt.show()
