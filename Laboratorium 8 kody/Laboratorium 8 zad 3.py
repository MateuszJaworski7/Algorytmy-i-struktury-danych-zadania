class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adj_matrix = [[0] * vertices for _ in range(vertices)]

    def add_edge(self, source, destination, weight=1):
        if source >= self.vertices or destination >= self.vertices:
            raise ValueError("Invalid vertex")

        self.adj_matrix[source][destination] = weight

    def get_adj_matrix(self):
        return self.adj_matrix

    def get_adj_list(self):
        adj_list = [[] for _ in range(self.vertices)]

        for i in range(self.vertices):
            for j in range(self.vertices):
                if self.adj_matrix[i][j] != 0:
                    adj_list[i].append((j, self.adj_matrix[i][j]))

        return adj_list

    def display_graph(self):
        print("Adjacency Matrix:")
        for row in self.adj_matrix:
            print(row)

        print("\nAdjacency List:")
        adj_list = self.get_adj_list()
        for vertex, neighbors in enumerate(adj_list):
            print(f"{vertex}: {neighbors}")

        print("\nGraph Visualization:")
        for i in range(self.vertices):
            row = ""
            for j in range(self.vertices):
                if self.adj_matrix[i][j] != 0:
                    row += f" -{self.adj_matrix[i][j]}-> {j}"
            if row:
                print(f"{i}{row}")


def main():
    while True:
        graph_type = input("Wybierz rodzaj grafu (skierowany/nieskierowany/ważony): ")

        if graph_type.lower() not in ["skierowany", "nieskierowany", "ważony", ]:
            print("Nieprawidłowy rodzaj grafu.")
            continue

        break

    while True:
        try:
            num_vertices = int(input("Podaj liczbę wierzchołków: "))
            if num_vertices <= 0:
                raise ValueError
            break
        except ValueError:
            print("Nieprawidłowa liczba wierzchołków.")

    graph = Graph(num_vertices)

    while True:
        try:
            num_edges = int(input("Podaj liczbę połączeń: "))
            if num_edges < 0:
                raise ValueError
            break
        except ValueError:
            print("Nieprawidłowa liczba połączeń.")




