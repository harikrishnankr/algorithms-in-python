def selection_sort(input_array):
    for i in range(len(input_array)):
        min_index = i
        for j in range(i+1, len(input_array)):
            if input_array[min_index] > input_array[j]:
                min_index = j

        input_array[i], input_array[min_index] = input_array[min_index], input_array[i]

    return input_array
