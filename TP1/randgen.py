import random as rand

def rand_list(n, v_min, v_max):
    tab = [0]*n #il est preferable de creer une liste tout de suite de la bonne taille
    for i in range(0,n) : 
        a = rand.randint(v_min, v_max)
        tab[i] = a
    return tab

#print(rand_list(10, 1, 8)) #list of 10 elements in [2,8]
#print(rand_list(250, 0, 13)) #bigger list