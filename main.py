# This is a sample Python script.
from algorithms.select_algorithms import execute_search_algorithm
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def execute_algorithm():
    print("Algorithms")
    print("1. Search")
    print("2. Sort")
    print("3. Greedy Algorithm")
    print("4. Dynamic Programming")
    algorithm = input("Select algorithm : ")

    if int(algorithm) == 1:
        execute_search_algorithm()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    execute_algorithm()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/