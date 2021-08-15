def get_array():
    lst = []
    size = int(input("Enter the number of elements : "))

    for i in range(0, size):
        item = int(input())
        lst.append(item)

    return lst
