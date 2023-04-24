n = int(input("Podaj liczbę naturalną z zakresu 1-20: "))
suma = 0
i = 1

while i <= n:
    suma += i*i
    i += 1

print(suma)
