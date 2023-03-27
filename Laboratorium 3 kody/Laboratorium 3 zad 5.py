def Hanoi(n, A, C, B):
    if n == 1:
        print("Przenieś dysk 1 z kołka", A, "na kołek", C)
        return
    Hanoi(n - 1, A, B, C)
    print("Przenieś dysk", n, "z kołka", A, "na kołek", C)
    Hanoi(n - 1, B, C, A)


n = 5
Hanoi(n, 'A', 'B', 'C')
