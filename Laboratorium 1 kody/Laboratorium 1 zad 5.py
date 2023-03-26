import random
import numpy as np

tab = np.random.randint(1,100,(5,5))
print (tab)

for j in range (tab.shape[0]):

    min=tab[j,0]
    min_id=0
    for i in range (tab.shape[1]):
        if tab[j,i]<min:
            min=tab[j,i]
            min_id=i
    tab[j,min_id]=tab[j,0]
    tab[j,0]=min


print (" ")
print (tab)
