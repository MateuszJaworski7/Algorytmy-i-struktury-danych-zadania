n = int(input("Podaj ilość ocen: "))
suma = 0
licznik = 0

while n>licznik:
    ocena = int(input("Podaj ocenę: "))
    if ocena == 0:
        break
    suma += ocena
    licznik += 1

srednia = suma/licznik

print(srednia)
