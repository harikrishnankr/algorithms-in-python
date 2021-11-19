def insertion_sort(input_array):
    for i in range(1, len(input_array)):
        min_val = input_array[j]
        j = i - 1
        while j >= 0 and input_array[j] > min_val:
            input_array[j + 1] = input_array[j]
            j -= 1
        input_array[j + 1] = min_val
    return input_array
