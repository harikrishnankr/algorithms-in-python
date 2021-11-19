def binary_search(input_array, left, right, find):
    if right >= left:
        mid = left + (right - left) // 2
        if input_array[mid] == find:
            return mid
        elif input_array[mid] > find:
            return binary_search(input_array, left, mid - 1, find)
        else:
            return binary_search(input_array, mid + 1, right, find)
    else:
        return -1
