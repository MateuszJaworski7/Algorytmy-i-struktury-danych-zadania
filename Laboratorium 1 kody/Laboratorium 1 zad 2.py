ile_u = 0
n = int(input("Podaj liczbę n: "))
if n>0:
    for i in range(n):
        x = int(input("Podaj liczbę: "))
        if x < 0:
            ile_u += 1
    print("Liczba ujemnych liczb w ciągu: ", ile_u)
else:
    print("Liczba nie jest większa od 0")
