def run_bfs(graph, node):
    queue = [node]
    while len(queue) > 0:
        current = queue.pop(0)
        print(current)
        for neighbour in graph[current]:
            queue.append(neighbour)


def bfs():
    adjacency_list = {
        "a": ["c", "b"],
        "b": ["d"],
        "c": ["e"],
        "d": ["f"],
        "e": [],
        "f": []
    }
    run_bfs(adjacency_list, "a")

