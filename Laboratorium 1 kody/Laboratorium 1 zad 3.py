import random
tab = []
for i in range(10):
    tab.append(random.randint(0,20))
print(tab)

x = int(input("podaj szukaną liczbę"))
if x in tab:
    print("podana wartość występuje w tablicy")
else:
    print("podana wartość nie występuje w tablicy")