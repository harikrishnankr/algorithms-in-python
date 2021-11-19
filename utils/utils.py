def get_array(is_float=False):
    lst = []
    size = int(input("Enter the number of elements : "))
    print("Enter the elements ::")
    for i in range(0, size):
        if is_float:
            item = int(input())
        else:
            item = float(input())
        lst.append(item)

    return lst
