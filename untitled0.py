# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 11:05:35 2020

@author: 49157
"""

task = {"a":(10,50),"b":(20,25),"c":(10,30), "d":(80, 15), "e":(60,30), "f":(20, 30) ,"g":(20, 30), "h":(30,120),
        "j":(10,30), "i":(25,30), "k":(25,30)}
res = []
import numpy as np
import itertools

for L in range(0, len(task.keys())+1):
    for subset in itertools.combinations(task.values(), L):
        res.append(subset)
def optimize_scrum_tasks(cost_limit):
    filtered_cost_with_benefit={}
    for s in res[1:]:
        if 0 < np.sum(s,axis=0)[0] <= cost_limit:
            filtered_cost_with_benefit[np.sum(s,axis=0)[1]] = s
    filtered_cost_with_benefit[np.max(list(filtered_cost_with_benefit.keys()))]
    cost = 0
    for pair in filtered_cost_with_benefit[np.max(list(filtered_cost_with_benefit.keys()))]:
        cost += pair[0]#print(cost)
    np.max(list(filtered_cost_with_benefit.keys())) #printing max benefit
    tuple_of_cost_benefit=tuple([i for i in task.values()])
#print(tuple_of_cost_benefit)

    li=set()
    for i in filtered_cost_with_benefit[np.max(list(filtered_cost_with_benefit.keys()))]:
        if i in tuple_of_cost_benefit:
            li.add((tuple_of_cost_benefit.index(i)))
    solution=sorted(li)#print((solution))
    return (cost,np.max(list(filtered_cost_with_benefit.keys())),solution)

print(optimize_scrum_tasks(1000))