# -*- coding:utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
import matplotlib

matplotlib.rcParams['font.family']='SimHei'
matplotlib.rcParams['font.size']=10


def f(t):
    return np.exp(-t)*np.cos(2*np.pi*t)

def test1():
    a=np.arange(0.0,5.0,0.02)
    plt.subplot(211)
    plt.plot(a,f(a))

    plt.plot(a,np.cos(2*np.pi*a),'r--')
    plt.show()

def test2():
    a=np.arange(10)
    plt.plot(a,a*1.5,'o--',a,a*2.5,'v-.',a,a*3.5,'1:',a,a*15)
    plt.ylabel('纵轴')
    plt.text(5,40,'哈哈')
    plt.title('一个例子 $y=cos(2\pi x)$')
    plt.show()

def test3(): #annotate
    a=np.arange(0.0,5.0,0.02)
    plt.plot(a,np.cos(2*np.pi*a),'r--')

    plt.xlabel('时间')
    plt.ylabel('振幅')
    plt.annotate(r'$mu=100$',xy=(2,1),xytext=(3,1.5),arrowprops=dict(facecolor='black',shrink=0.1,width=2))
    plt.axis([-1,6,-2,2])
    plt.grid(True)
    plt.show()

def test4(): # subplot2grid
    plt.subplot2grid((3,3),(1,2),rowspan=2)
    a = np.arange(0.0, 5.0, 0.02)
    plt.plot(a, np.cos(2 * np.pi * a), 'r--')
    plt.show()

def test5(): #gridspec
    import matplotlib.gridspec as gridspec
    gs=gridspec.GridSpec(3,3)

    # ax1=plt.subplot(gs[0,:])
    ax2=plt.subplot(gs[1,:2])

    a = np.arange(0.0, 5.0, 0.02)
    plt.plot(a, np.cos(2 * np.pi * a), 'r--')
    plt.show()

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




multi_figure()