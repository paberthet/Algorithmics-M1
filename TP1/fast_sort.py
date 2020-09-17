# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 09:28:45 2020

@author: Jan Mejro
"""

import randgen as rg

def fast_sort(tab):
    n = len(tab)
    if(n <= 1):
        return tab
    elif(n==2):
        if(tab[0]>tab[1]):
            tab[0],tab[1] = tab[1],tab[0]
        return tab
    else:
        pivot = n//2
        tab[pivot],tab[n-1] = tab[n-1], tab[pivot]
        j = 0
        for i in range(0, n-1):
            if(tab[i] < tab[n-1]):
                tab[i],tab[j] = tab[j], tab[i]
                j +=1
        tab[j],tab[n-1] = tab[n-1],tab[j]
        return fast_sort(tab[:j]) + [tab[j]] + fast_sort(tab[j+1:])


tab = rg.rand_list(25,0,9)
#print(tab)
#print(fast_sort(tab))