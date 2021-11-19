def bubble_sort(input_array):
    size = len(input_array)
    for i in range(size):
        for j in range(0, size-i-1):
            if input_array[j] > input_array[j+1]:
                input_array[j], input_array[j+1] = input_array[j+1], input_array[j]
    return input_array
