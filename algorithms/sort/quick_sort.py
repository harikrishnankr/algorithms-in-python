def partition(input_array, left, right):
    pivot = input_array[right]
    min_index = left - 1

    # j : left to (right - 1)
    for i in range(left, right):
        if input_array[i] < pivot:
            min_index += 1
            input_array[min_index], input_array[i] = input_array[i], input_array[min_index]

    input_array[min_index + 1], input_array[right] = input_array[right], input_array[min_index + 1]
    return min_index + 1


def quick_sort(input_array, left, right):
    if left < right:
        p = partition(input_array, left, right)

        quick_sort(input_array, left, p - 1)
        quick_sort(input_array, p + 1, right)

    return input_array
