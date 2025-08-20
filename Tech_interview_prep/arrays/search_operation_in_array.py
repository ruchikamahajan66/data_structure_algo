def search_operation(arr, x):
    for i in range(0, len(arr)):
        if arr[i] == x:
            return i
    return -1


if __name__ == '__main__':
    arr = [20, 5, 7, 25]
    x = 35
    print("found element in array at index", search_operation(arr, x))
