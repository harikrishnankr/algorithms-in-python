# This is a sample Python script.

from algorithms.search.select_algorithms import execute_search_algorithm
from algorithms.sort.select_algorithm import execute_sort_algorithm
from algorithms.greedy.select_algorithm import select_greedy_algorithm
from algorithms.spiral_matrix import spiral_matrix
from algorithms.graph.select_algorithm import select_graph_algorithms
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def execute_algorithm():
    print("Algorithms")
    print("1. Search")
    print("2. Sort")
    print("3. Greedy Algorithm")
    print("4. Dynamic Programming")
    print("5. Graphs")
    print("6. Spiral matrix")
    algorithm = input("Select algorithm : ")

    if int(algorithm) == 1:
        execute_search_algorithm()
    elif int(algorithm) == 2:
        execute_sort_algorithm()
    elif int(algorithm) == 3:
        select_greedy_algorithm()
    elif int(algorithm) == 5:
        select_graph_algorithms()
    elif int(algorithm) == 6:
        spiral_matrix()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    execute_algorithm()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
