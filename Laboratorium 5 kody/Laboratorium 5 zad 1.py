def fib_dyn(n):
    if n == 0:
        return 0
    elif n==1:
        return 1
    elif n>1:
        T = [0, 1]
        i = 2
        while (i<=n):
            T.append(T[i-1]+T[i-2])
            i+=1
        return T[i-1]

n=int(input("podaj n: "))
if(n>0):
    print(fib_dyn(n))
else:
    print("podano złe dane")



