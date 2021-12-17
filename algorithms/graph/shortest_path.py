def build_graph(edges):
    graph = {}
    for edge in edges:
        s, d = edge
        if s not in graph:
            graph[s] = []
        if d not in graph:
            graph[d] = []
        graph[s].append(d)
        graph[d].append(s)

    return graph


def find_shortest_path(graph, node_a, node_b):
    # It would be better if we use breadth first search for shortest path find
    visited = set()
    queue = [[node_a, 0]]

    while len(queue) > 0:
        node, distance = queue.pop(0)
        if node == node_b:
            return distance
        for neighbour in graph[node]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append([neighbour, distance + 1])

    return -1


def shortest_path():
    edges = [
        ["w", "x"],
        ["x", "y"],
        ["z", "y"],
        ["z", "v"],
        ["w", "v"]
    ]
    graph = build_graph(edges)
    print(f"{find_shortest_path(graph, 'w', 'z')}")
