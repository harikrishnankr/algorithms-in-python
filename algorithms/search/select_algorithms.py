from algorithms.search.linear import liner_search
from algorithms.search.binary import binary_search
from algorithms.search.jump import jump_search
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
        index = liner_search(input_array, int(find))
        print(f"Value is in {index} index")

    elif int(algorithms) == 2:
        print("::::Array should be sorted for binary search::::")
        input_array = get_array()
        find = input("Enter the value to search : ")
        index = binary_search(input_array, 0, len(input_array), int(find))
        print(f"Value is in {index} index")

    elif int(algorithms) == 3:
        print("::::Array should be sorted for binary search::::")
        input_array = get_array()
        find = input("Enter the value to search : ")
        index = jump_search(input_array, int(find))
        print(f"Value is in {index} index")

    else:
        print("No such Algorithm exists in our system")
