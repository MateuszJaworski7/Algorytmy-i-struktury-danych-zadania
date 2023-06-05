from collections import deque

def bfs(G, start):
    odw = set()
    queue = deque([start])

    while queue:
        vertex = queue.popleft()
        print(vertex)

        if vertex not in odw:
            odw.add(vertex)

            for x in G[vertex]:
                if x not in odw:
                    queue.append(x)
G = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

bfs(G, 'A')
