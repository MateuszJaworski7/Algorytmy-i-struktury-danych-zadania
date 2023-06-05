def dfs(G, start, odw=None):
    if odw is None:
        odw = set()
    odw.add(start)
    print(start)
    for x in G[start]:
        if x not in odw:
            dfs(G, x, odw)
G = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

dfs(G, 'A')
