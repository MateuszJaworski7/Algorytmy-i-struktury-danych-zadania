
class Graph:
    def __init__(self, z):
        self.V = z
        self.graph = []

    def krawedz(self, u, v, w):
        self.graph.append([u, v, w])

    def find(self, rodzic, i):
        if rodzic[i] == i:
            return i
        return self.find(rodzic, rodzic[i])

    def zap(self, rodzic, ranga, x, y):
        xx = self.find(rodzic, x)
        yy = self.find(rodzic, y)
        if ranga[xx] < ranga[yy]:
            rodzic[xx] = yy
        elif ranga[xx] > ranga[yy]:
            rodzic[yy] = xx
        else:
            rodzic[yy] = xx
            ranga[xx] += 1

    def kruskal_algo(self):
        wynik = []
        i, e = 0, 0
        self.graph = sorted(self.graph, key=lambda item: item[2])
        rodzic = []
        ranga = []
        for node in range(self.V):
            rodzic.append(node)
            ranga.append(0)
        while e < self.V - 1:
            u, v, w = self.graph[i]
            i = i + 1
            x = self.find(rodzic, u)
            y = self.find(rodzic, v)
            if x != y:
                e = e + 1
                wynik.append([u, v, w])
                self.zap(rodzic, ranga, x, y)
        for u, v, waga in wynik:
            print("%d - %d: %d" % (u, v, waga))


g = Graph(6)
g.krawedz(0, 1, 4)
g.krawedz(0, 2, 4)
g.krawedz(1, 2, 2)
g.krawedz(1, 0, 4)
g.krawedz(2, 0, 4)
g.krawedz(2, 1, 2)
g.krawedz(2, 3, 3)
g.krawedz(2, 5, 2)
g.krawedz(2, 4, 4)
g.krawedz(3, 2, 3)
g.krawedz(3, 4, 3)
g.krawedz(4, 2, 4)
g.krawedz(4, 3, 3)
g.krawedz(5, 2, 2)
g.krawedz(5, 4, 3)
g.kruskal_algo()