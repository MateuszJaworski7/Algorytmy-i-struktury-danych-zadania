
INF = 9999999
V = 5
G = [[0, 9, 75, 0, 0],
     [9, 0, 95, 19, 42],
     [75, 95, 0, 51, 66],
     [0, 19, 51, 0, 31],
     [0, 42, 66, 31, 0]]

s = [0, 0, 0, 0, 0]
bkra = 0
s[0] = True
print("Krawędź : Waga\n")
while (bkra < V - 1):
    min = INF
    x = 0
    y = 0
    for i in range(V):
        if s[i]:
            for j in range(V):
                if ((not s[j]) and G[i][j]):
                    if min > G[i][j]:
                        min = G[i][j]
                        x = i
                        y = j
    print(str(x) + "-" + str(y) + ":" + str(G[x][y]))
    s[y] = True
    bkra += 1