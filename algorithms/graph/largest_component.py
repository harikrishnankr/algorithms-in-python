def traverse(graph, node, visited, node_count):
    if node in visited:
        return node_count

    visited.add(node)
    node_count += 1

    for neighbour in graph[node]:
        node_count = traverse(graph, neighbour, visited, node_count)

    return node_count


def largest_component():
    graph = {
        "0": ["8", "1", "5", "4"],
        "1": ["0"],
        "5": ["0", "8"],
        "8": ["0", "5"],
        "2": ["3", "4"],
        "3": ["2", "4"],
        "4": ["3", "2", "0"]
    }
    visited = set()
    node_count = 0

    for node in graph:
        count = traverse(graph, node, visited, 0)
        if node_count < count:
            node_count = count

    print(node_count)
