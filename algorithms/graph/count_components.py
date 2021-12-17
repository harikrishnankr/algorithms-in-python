def graph_count(graph, node, visited_nodes):
    if node in visited_nodes:
        return False

    visited_nodes.add(node)
    for neighbour in graph[node]:
        graph_count(graph, neighbour, visited_nodes)

    return True


def count_components():
    graph = {
        "3": [],
        "4": [],
        "6": ["4", "5", "7", "8"],
        "8": ["6"],
        "7": ["6", "5"],
        "5": ["6", "7"],
        "1": ["2"],
        "2": ["1"]
    }
    visited_nodes = set()
    count = 0
    for node in graph:
        if graph_count(graph, node, visited_nodes):
            count += 1

    print(count)
