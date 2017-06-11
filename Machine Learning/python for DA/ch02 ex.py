# -*- coding:utf-8 -*-
import json

path='data/ch02/usagov_bitly_data2012-03-16-1331923249.txt'

records=[json.loads(line) for line in open(path)]
time_zones=[rec['tz'] for rec in records if 'tz' in rec]

def get_counts(sequense):
    counts={}
    for x in sequense:
        if x in counts:
            counts[x]+=1
        else:
            counts[x]=1
    return counts


print(get_counts(time_zones))