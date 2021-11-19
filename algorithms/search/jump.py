import math


def jump_search(input_array, find):
    size = len(input_array)
    step_diff = math.sqrt(size)
    pointer = 0

    while input_array[int(min(step_diff, size)) - 1] < find:
        pointer = step_diff
        step_diff += math.sqrt(size)

        if pointer >= size:
            return -1

    while input_array[int(pointer)] < find:
        pointer += 1

        if pointer >= min(step_diff, size):
            return -1

    if input_array[int(pointer)] == find:
        return int(pointer)

    return -1