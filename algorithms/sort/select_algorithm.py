from utils.utils import get_array
from algorithms.sort.bubble import bubble_sort
from algorithms.sort.selection_srot import selection_sort
from algorithms.sort.insertion_sort import insertion_sort
from algorithms.sort.merge_sort import merge_sort
from algorithms.sort.heap_sort import heap_sort
from algorithms.sort.quick_sort import quick_sort
from algorithms.sort.radix_sort import radix_sort
from algorithms.sort.bucket_sort import bucket_sort


def execute_sort_algorithm():
    print("Select Search Algorithm")
    print("1. Bubble Sort")
    print("2. Selection Sort")
    print("3. Insertion Sort")
    print("4. Merge Sort")
    print("5. Heap Sort")
    print("6. Quick Sort")
    print("7. Radix Sort")
    print("8. Bucket Sort")
    algorithms = input("Enter Algorithm : ")

    if int(algorithms) == 1:
        input_array = get_array()
        sorted_array = bubble_sort(input_array)
        print(f"Sorted array {sorted_array}")

    elif int(algorithms) == 2:
        input_array = get_array()
        sorted_array = selection_sort(input_array)
        print(f"Sorted array {sorted_array}")

    elif int(algorithms) == 3:
        input_array = get_array()
        sorted_array = insertion_sort(input_array)
        print(f"Sorted array {sorted_array}")

    elif int(algorithms) == 4:
        input_array = get_array()
        sorted_array = merge_sort(input_array, 0, len(input_array) - 1)
        print(f"Sorted array {sorted_array}")

    elif int(algorithms) == 5:
        input_array = get_array()
        sorted_array = heap_sort(input_array)
        print(f"Sorted array {sorted_array}")

    elif int(algorithms) == 6:
        input_array = get_array(True)
        sorted_array = quick_sort(input_array, 0, len(input_array) - 1)
        print(f"Sorted array {sorted_array}")

    elif int(algorithms) == 7:
        input_array = get_array()
        sorted_array = radix_sort(input_array)
        print(f"Sorted array {sorted_array}")

    elif int(algorithms) == 8:
        input_array = get_array()
        sorted_array = bucket_sort(input_array)
        print(f"Sorted array {sorted_array}")

    else:
        print("No such Algorithm exists in our system")

