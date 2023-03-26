
import random

def min(tab):
    m=tab[0]
    for i in tab:
        if i<m:
            m=i
    return m

tab=[]
for i in range(10):
    tab.append(random.randint(0,20))
print(tab)
print(min(tab))

