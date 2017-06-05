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

