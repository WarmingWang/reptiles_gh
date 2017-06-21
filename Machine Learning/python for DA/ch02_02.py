# -*- coding:utf-8 -*-

import pandas as pd
import numpy as np

unames=['user_id','gender','age','occupation','zip']
users=pd.read_table('DATA/ch02/movielens/users.dat',sep='::',header=None,names=unames,engine='python')

rnames=['user_id','movie_id','rating','timestamp']
ratings=pd.read_table('DATA/ch02/movielens/ratings.dat',sep='::',header=None,names=rnames,engine='python')

mnames=['movie_id','title','genres']
movies=pd.read_table('DATA/ch02/movielens/movies.dat',sep='::',header=None,names=mnames,engine='python')

data=pd.merge(pd.merge(ratings,users),movies)
mean_ratings=data.pivot_table(values='rating',index=['title'],columns=['gender'],aggfunc=np.mean)  #aggfunc默认为np.mean
mean_ratings.to_csv('test3.csv')

rating_by_title=data.groupby(['title']).size()
active_title=rating_by_title.index[rating_by_title>=250]
active_mean_rating=mean_ratings.ix[active_title]

top_female_ratings=active_mean_rating.sort_values(by='F',ascending=False)

active_mean_rating['diff']=active_mean_rating['M']-active_mean_rating['F']
sort_by_diff=active_mean_rating.sort_values(by='diff')

std_by_title=data.groupby('title')['rating'].std()
rating_std_by_title=std_by_title.ix[active_title]
std_order=rating_std_by_title.sort_values(ascending=False)[:10]    #现行版本pandas对DataFrame、Series排序统一用.sort_values()方法
print(std_order)
