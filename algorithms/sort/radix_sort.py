def counting_sort(input_array, exponent, max_value):
    n = len(input_array)

    output = [0] * n
    count = [0] * 10

    for i in range(0, n):
        significant_position = input_array[i] // exponent
        count[significant_position % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = input_array[i] // exponent
        output[count[index % 10] - 1] = input_array[i]
        count[index % 10] -= 1
        i -= 1

    i = 0
    for i in range(0, len(input_array)):
        input_array[i] = output[i]

    return input_array


def radix_sort(input_array):
    max_value = max(input_array)

    exponent = 1
    while max_value / exponent > 0:
        counting_sort(input_array, exponent, max_value)
        exponent *= 10

    return input_array
