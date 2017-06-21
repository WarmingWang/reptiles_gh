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
mean_ratings=data.pivot_table(values='rating',index=['title'],columns=['gender'],aggfunc=np.mean)

rating_by_title=data.groupby(['title']).size()
active_title=rating_by_title.index[rating_by_title>=250]
active_mean_rating=mean_ratings.ix[active_title]
print(active_mean_rating)

