## Python lists don’t automatically expand like C arrays.
###That is why we need to add dummy element at the end of the list first


def insert_operation(arr, pos, x):
    if len(arr) == pos:
        return arr
    idx = pos - 1
    arr.append(0)

    for i in range(len(arr) - 2, idx - 1, -1):
        arr[i + 1] = arr[i]
    arr[idx] = x
    return arr


if __name__ == '__main__':
    arr = [5, 3, 7, 10, 20]
    x = 8
    pos = 2
    print(arr)
    print("new array is", insert_operation(arr, pos, x))
