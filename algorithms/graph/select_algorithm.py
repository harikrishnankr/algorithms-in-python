from algorithms.graph.dfs import dfs
from algorithms.graph.bfs import bfs
from algorithms.graph.count_components import count_components
from algorithms.graph.largest_component import largest_component
from algorithms.graph.shortest_path import shortest_path


def select_graph_algorithms():
    print("Select Graph Algorithm")
    print("1. DFS")
    print("2. BFS")
    print("3. Count Components")
    print("4. Largest Component")
    print("5. Shortest Path")

    algorithm = input("Enter Algorithm : ")

    if int(algorithm) == 1:
        dfs()
    elif int(algorithm) == 2:
        bfs()
    elif int(algorithm) == 3:
        count_components()
    elif int(algorithm) == 4:
        largest_component()
    elif int(algorithm) == 5:
        shortest_path()
