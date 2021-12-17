def heapify(input_array, heap_size, node_index):
    largest_item_index = node_index
    left_index = (2 * node_index) + 1
    right_index = (2 * node_index) + 2

    if left_index < heap_size and input_array[left_index] > input_array[largest_item_index]:
        largest_item_index = left_index

    if right_index < heap_size and input_array[right_index] > input_array[largest_item_index]:
        largest_item_index = right_index

    if largest_item_index != node_index:
        input_array[largest_item_index], input_array[node_index] = input_array[node_index],\
                                                                   input_array[largest_item_index]
        heapify(input_array, heap_size, largest_item_index)


def heap_sort(input_array):
    n = len(input_array)
    # range(start, stop +- 1, step)
    for i in range(int(n/2) - 1, -1, -1):
        heapify(input_array, n, i)

    print(input_array)

    for i in range(n - 1, 0, -1):
        input_array[0], input_array[i] = input_array[i], input_array[0]
        heapify(input_array, i, 0)

    return input_array
