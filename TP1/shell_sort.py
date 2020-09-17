# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 09:12:33 2020

@author: Jan Mejro
"""

import randgen as rg
""" version perso
def jump_creator(tab):
    n = len(tab)
    tab2 = [701,301,132,57,23,10,4,1]
    for i in range(len(tab2)-1,0,-1):
        if(n<tab2[i]):
            tab2 = tab2[i+1:]
            break
    return tab2
  """
  
def jump_creator(tab): #version par comprehension de liste
    n = len(tab)
    jumps = [1,4,10,23,57,132,301,701]
    [e for e in jumps if e < n]
    jumps.reverse()
    return jumps

def shell_sort(tab):
    n = len(tab)
    jumps = jump_creator(tab)
    for h in jumps:
        for i in range(h , n):
            temp = tab[i]
            j = i
            while( j >= h and tab[j-h] > temp):
                tab[j] = tab[j-h]
                j = j-h
            tab[j] = temp
    return tab

tab = rg.rand_list(25,0,9)
#tab = rg.rand_list(1000,0,9) #big list testing for jump_creator
#print(jump_creator(tab))
#print(tab)
#print(shell_sort(tab))
