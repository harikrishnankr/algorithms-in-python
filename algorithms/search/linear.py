def liner_search(input_array, search_input):
    for i in range(0, len(input_array)):
        if input_array[i] == search_input:
            return i + 1
    return -1
