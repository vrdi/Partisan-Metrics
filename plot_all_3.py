# -*- coding: utf-8 -*-
"""
Created on Sun Jul  7 20:42:33 2019

@author: daryl
"""

import matplotlib.pyplot as plt
import numpy as np
def partisan_symmetry(vec):
    vec = sorted(vec)
    return (4/3)*abs(np.mean(vec)-vec[1])

for k in range(1,100):
    a=[]
    for i in range(1,100):
        a.append([])
        for j in range(1,100):
            a[i-1].append(partisan_symmetry([i/100,k/100,j/100]))

    plt.imshow(a)
    plt.colorbar()#plt.colorbar(boundaries=[x/20 for x in range(10)]) #
    plt.xticks(range(0,100,5))#(range(99),[x/100 for x in range(1,100)])
    plt.yticks(range(0,100,5))#(range(99),[x/100 for x in range(1,100)])
    plt.title("Partisan Gini for (x%,"+str(k)+"%,y%)")
    plt.savefig("./ps"+str(k).zfill(2) +".png")
    plt.close()
    print("figure",k,"done")
