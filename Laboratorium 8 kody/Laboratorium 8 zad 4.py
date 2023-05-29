import sys


class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adj_matrix = [[0] * vertices for _ in range(vertices)]

    def add_edge(self, source, destination, weight):
        if source >= self.vertices or destination >= self.vertices:
            raise ValueError("Invalid vertex")

        self.adj_matrix[source][destination] = weight
        self.adj_matrix[destination][source] = weight

    def dijkstra(self, source):
        distance = [sys.maxsize] * self.vertices
        distance[source] = 0
        visited = [False] * self.vertices

        for _ in range(self.vertices):
            min_distance = sys.maxsize
            min_vertex = None

            for v in range(self.vertices):
                if not visited[v] and distance[v] < min_distance:
                    min_distance = distance[v]
                    min_vertex = v

            if min_vertex is None:
                break

            visited[min_vertex] = True

            for v in range(self.vertices):
                if (
                        not visited[v]
                        and self.adj_matrix[min_vertex][v] != 0
                        and distance[min_vertex] + self.adj_matrix[min_vertex][v] < distance[v]
                ):
                    distance[v] = distance[min_vertex] + self.adj_matrix[min_vertex][v]

        return distance

    def display_shortest_paths(self, source):
        distances = self.dijkstra(source)

        print(f"Shortest paths from vertex {source}:")
        for v in range(self.vertices):
            print(f"To vertex {v}: Distance = {distances[v]}")


def main():
    graph = Graph(6)
    graph.add_edge(0, 1, 7)
    graph.add_edge(0, 2, 9)
    graph.add_edge(0, 5, 14)
    graph.add_edge(1, 2, 10)
    graph.add_edge(1, 3, 15)
    graph.add_edge(2, 3, 11)
    graph.add_edge(2, 5, 2)
    graph.add_edge(3, 4, 6)
    graph.add_edge(4, 5, 9)

    source_vertex = 0
    graph.display_shortest_paths(source_vertex)
