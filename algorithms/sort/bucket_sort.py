from algorithms.sort.insertion_sort import insertion_sort


def bucket_sort(input_array):
    bucket_array = []
    slot_number = 10

    for i in range(slot_number):
        bucket_array.append([])

    for elm in input_array:
        index = int(slot_number * elm)
        bucket_array[index].append(elm)

    for i in range(slot_number):
        bucket_array[i] = insertion_sort(bucket_array[i])

    c = 0
    for i in range(slot_number):
        for bucket_index in range(len(bucket_array[i])):
            input_array[c] = bucket_array[i][bucket_index]
            c += 1

    return input_array
