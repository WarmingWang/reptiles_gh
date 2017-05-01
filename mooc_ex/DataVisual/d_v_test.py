# -*- coding:utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
import matplotlib

matplotlib.rcParams['font.family']='SimHei'
matplotlib.rcParams['font.size']=16


def f(t):
    return np.exp(-t)*np.cos(2*np.pi*t)

def test1():
    a=np.arange(0.0,5.0,0.02)
    plt.subplot(211)
    plt.plot(a,f(a))

    plt.subplot(212)
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

test5()