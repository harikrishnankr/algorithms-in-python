def merge(input_array, left, mid, right):
    left_array = input_array[left:mid+1]
    right_array = input_array[mid+1:right+1]

    i = j = 0
    k = left

    while i < len(left_array) and j < len(right_array):
        if left_array[i] <= right_array[j]:
            input_array[k] = left_array[i]
            i += 1
        else:
            input_array[k] = right_array[j]
            j += 1
        k += 1

    while i < len(left_array):
        input_array[k] = left_array[i]
        i += 1
        k += 1

    while j < len(right_array):
        input_array[k] = right_array[j]
        j += 1
        k += 1


def merge_sort(input_array, left, right):

    if left >= right:
        return

    mid_point = left + ((right - left) // 2)

    # Split the input array into two halves
    merge_sort(input_array, left, mid_point)
    merge_sort(input_array, mid_point + 1, right)

    # Sort then merge the sub arrays
    merge(input_array, left, mid_point, right)

    return input_array

