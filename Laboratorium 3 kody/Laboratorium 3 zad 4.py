def zamiana(a):
    if a == 0:
        return '0'
    else:
        p = a % 2
        x = a // 2
        y = zamiana(x)
        return str(p) + y

print(zamiana(5))
print(zamiana(30))