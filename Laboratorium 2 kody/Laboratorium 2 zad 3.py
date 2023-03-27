def funkcja(L):
    L = list(map(str, L))
    M = sorted(L)
    M = list(map(int, M))

    return M
L = [1, 2, 3, 11, 21, 111, 231]
M = funkcja(L)
print(M)