import math


def spiral_matrix():
    matrix = [
        [1, 2, 3, 4, 5],
        [16, 17, 18, 19, 6],
        [15, 24, 25, 20, 7],
        [14, 23, 22, 21, 8]
    ]
    m = 4
    n = 5
    t = 0
    left = 0
    right = n - 1
    top = 0
    bottom = m - 1
    direction = 0

    while t < (m * n):
        if direction == 0:
            for i in range(left, right + 1):
                print(matrix[top][i])
                t += 1
            top += 1

        elif direction == 1:
            for i in range(top, bottom + 1):
                print(matrix[i][right])
                t += 1
            right -= 1

        elif direction == 2:
            for i in range(right, left - 1, -1):
                print(matrix[bottom][i])
                t += 1
            bottom -= 1

        elif direction == 3:
            for i in range(bottom, top - 1, -1):
                print(matrix[i][left])
                t += 1
            left += 1

        direction += 1

        if direction == 4:
            direction = 0
