def najwiekszy_element(W, l, r):
    if l == r:
        return W[l]
    srodek = (l + r) // 2
    lewa = najwiekszy_element(W, l, srodek)
    prawa = najwiekszy_element(W, srodek + 1, r)
    if lewa > prawa:
        return lewa
    else:
        return prawa
print(najwiekszy_element([20,14,18,45,32,68,44,53],0,7))