# -*- coding:utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
import matplotlib
import pandas as pd

matplotlib.rcParams['font.family']='SimHei'
matplotlib.rcParams['font.size']=10


def f(t):
    return np.exp(-t)*np.cos(2*np.pi*t)

def plot_pie():
    labels='Frogs','Hogs','Dogs','Logs'
    sizes=[15,30,45,10]
    explode=[0,0.1,0,0]

    plt.pie(sizes,explode=explode,labels=labels,autopct='%1.1f%%',shadow=False,startangle=90)
    plt.axis('equal')

    plt.show()

def plot_hist():
    np.random.seed(2)
    mu,sigma=100,20
    a=np.random.normal(mu,sigma,size=100)

    plt.hist(a,20,normed=0,histtype='barstacked',facecolor='b',alpha=0.75)
    plt.title('直方图')

    plt.show()

def plot_polar():
    np.random.seed(0)
    n=20
    theta=np.linspace(0.0,2*np.pi,n,endpoint=False)
    radii=10*np.random.rand(n)
    width=np.pi/4*np.random.rand(n)

    import matplotlib.gridspec as gridspec
    gs=gridspec.GridSpec(4,4)
    ax=plt.subplot(gs[:3,:3],projection='polar')
    bars=ax.bar(theta,radii,width=width,bottom=0.0)


    for r,bar in  zip(radii,bars):
        bar.set_facecolor(plt.cm.viridis(r/10.))
        bar.set_alpha(0.5)


    plt.show()

def multi_figure():
    # np.random.seed(0)
    # x=np.random.rand(0,2*np.pi,100)
    # fig1=plt.figure()
    # fig2=plt.figure()
    #
    plt.figure(1)  # the first figure
    plt.subplot(211)  # the first subplot in the first figure
    plt.plot([1, 2, 3])
    plt.subplot(212)  # the second subplot in the first figure
    plt.plot([4, 5, 6])

    plt.figure(2)  # a second figure
    plt.plot([4, 5, 6])  # creates a subplot(111) by default

    plt.figure(1)  # figure 1 current; subplot(212) still current
    plt.subplot(211)  # make subplot(211) in figure1 current
    plt.title('Easy as 1, 2, 3')  # subplot 211 title

    plt.show()

def shape_test():
    a=np.arange(20).reshape(4,5)
    print(a)
    print(a.shape[0])

def pd_test():
    d=pd.Series({'a':9,'b':8,'c':7})
    print(d)


pd_test()
