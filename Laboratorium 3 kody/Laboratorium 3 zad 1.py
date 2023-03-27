def silnia(n):
    if(n==0):
         return 1
    return silnia (n-1)*n

print("podaj n")
a = int(input())
print(silnia(a))


def NWD(a,b):
    while a!=b:
        if a>b:
            a = a-b;
        else: b = b-a;
    return a
print(NWD(12,18))
print(NWD(28,24))



def NWDrek(a,b):
    if a!=b:
        if a>b: return NWDrek(a-b,b)
        else: return NWDrek(a, b-a)
    return a;

print(NWDrek(12,18))
print(NWDrek(28,24))



def nwdII(a,b):
    while b!=0:
        temp = b
        b = a % b
        a = temp
    return a

def nwdIIrek(a,b):
    if b!=0:
        return nwdIIrek(b, a % b)
    return a

