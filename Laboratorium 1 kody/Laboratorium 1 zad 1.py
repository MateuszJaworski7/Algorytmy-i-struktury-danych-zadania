import math
a = int(input("podaj a"))
b = int(input("podaj b"))
c = int(input("podaj c"))

if a==0:
    print("Nie jest to równanie kwadratowe")
else:
    d = b*b-4*a*c
    if d>0:
        x1=(-b-math.sqrt(d))/(2*a)
        x2=(-b+math.sqrt(d))/(2*a)
        print(x1,x2)
    else:
        if d == 0:
            x1=-b/(2*a)
            print(x1)
        else:
            print("Brak rozwiązań rzeczywistych")
