def run_dfs(graph, node):
    stack = [node]
    while len(stack) > 0:
        current = stack.pop()
        print(current)
        for neighbour in graph[current]:
            stack.append(neighbour)


def run_recursive_dfs(graph, node):
    print(node)
    for neighbour in graph[node]:
        run_recursive_dfs(graph, neighbour)


def dfs():
    adjacency_list = {
        "a": ["b", "c"],
        "b": ["d"],
        "c": ["e"],
        "d": ["f"],
        "e": [],
        "f": []
    }
    run_dfs(adjacency_list, "a")
    run_recursive_dfs(adjacency_list, "a")

