# from search.linear import liner_search
from algorithms.search.linear import liner_search
from utils.utils import get_array


def execute_search_algorithm():
    print("Select Search Algorithm")
    print("1. Linear Search")
    print("2. Binary Search")
    print("3. Jump Search")
    print("4. Interpolation Search")
    print("5. Exponential Search")
    print("6. Ternary Search")
    algorithms = input("Enter Algorithm : ")

    if int(algorithms) == 1:
        input_array = get_array()
        find = input("Enter the value to search : ")
        index = liner_search(input_array, find)
        print(f"Value is in {index} index")
