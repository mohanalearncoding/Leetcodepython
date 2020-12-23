from math import floor
from operator import itemgetter
from statistics import mean
from typing import List


def highFive( item: List[List[int]]) -> List[List[int]]:
    #[[1, 91], [1, 92], [2, 93], [2, 97], [1, 60], [2, 77], [1, 65], [1, 87], [1, 100], [2, 100], [2, 76]]
    d={}

    for i,k in item:
          if i not in d:
              d[i]=[]
          d[i].append(k)
    a =[]
    for key in sorted(d):
        d[key] = sorted(d[key],reverse=True)
        s=floor(mean((d[key][0:5])))
        a.append([key,s])
    #print(d)
    return a
print(highFive([[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]]))
