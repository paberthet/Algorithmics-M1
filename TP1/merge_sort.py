# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 11:09:36 2020

@author: Jan Mejro
"""

import randgen as rg

def merging_ms(tab1,tab2):
    n = len(tab1)
    m = len(tab2)
    tab = [0]*n + [0]*m
    k = 0
    while n>0 and m>0:
        #On triche un peu
        #du fait des split on sait que les deux tableaux sont deja tries
        if(tab1[0]<tab2[0]): #voila pk on compare les indices 0
            tab[k] = tab1[0] #le tableau gagnant confere sa valeur
            del(tab1[0]) #le tableau gagnant se voit reduit
            n-=1
            k+=1 #on passe a la case suivante
        else:
            tab[k] = tab2[0] #mm comments que la boucle precedente
            del(tab2[0])
            m-=1
            k+=1
    if(n ==0): #on detecte lequel des tableaux est vide
        tab = tab[:k] + tab2
    else:
        tab = tab[:k] + tab1
    return tab

#print(merging_ms([1,1,2,3], [1,2,5,5]))

def merge_sort(tab):
    n = len(tab)
    if (n <= 1):
        return tab
    else:
        split = n//2
        tab1 = merge_sort(tab[:split]) #on continue a split recursivement
        tab2 = merge_sort(tab[split:])
        return merging_ms(tab1,tab2) #on merge recursivement
    #si on represente les operations on split en descendant un arbre
    #que l on remonte avec des merges
    
tab = rg.rand_list(25,0,9)
print(tab)
print(merge_sort(tab))