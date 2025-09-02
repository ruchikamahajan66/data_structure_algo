def reverse(arr):
    low = 0
    high = len(arr) - 1

    while low < high:
        temp = arr[low]
        arr[low] = arr[high]
        arr[high] = temp

        low = low + 1
        high = high - 1


if __name__ == '__main__':
    array1 = [10, 5, 7, 30]
    array2 = [30, 7, 5, 10]
    print(reverse(array1))
