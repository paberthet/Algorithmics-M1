import randgen as rg
def insert_sort_rlist(n,v_min,v_max): #function that generates the list
    tab = rg.rand_list(n,v_min,v_max)
    for i in range(0,n-1):
        i_min = i
        for j in range(i + 1, n):
            if tab[j] < tab[i_min] :
                i_min = j
        if i_min != i : 
            tab[i_min],tab[i] = tab[i],tab[i_min]
    return tab

def insert_sort(tab): #function using a pregenerated list
    n = len(tab)
    for i in range(0,n-1):
        i_min = i
        for j in range(i + 1, n):
            if tab[j] < tab[i_min] :
                i_min = j
        if i_min != i : 
            tab[i_min],tab[i] = tab[i],tab[i_min]
    return tab

#print(insert_sort_rlist(10, 2, 8))
tab = rg.rand_list(10,2,8)
#print(tab)
#print(insert_sort(tab))