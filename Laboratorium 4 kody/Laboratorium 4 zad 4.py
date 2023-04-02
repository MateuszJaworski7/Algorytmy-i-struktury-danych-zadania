def suma(W, l, r):
    if l == r:
        return W[l]
    srodek = (l + r) // 2
    lewa = suma(W, l, srodek)
    prawa = suma(W, srodek + 1, r)
    return lewa + prawa
print(suma([12,14,27,89,72,54],0,5))
