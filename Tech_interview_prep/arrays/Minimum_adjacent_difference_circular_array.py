def minAdjDiff(arr):
    min = abs(arr[len(arr) - 1] - arr[0])
    for i in range(0, len(arr)-1):
        arr[i] = abs(arr[i] - arr[i+1])
        if arr[i] < min:
            min =  arr[i]
    return min


if __name__ == '__main__':
    # array = [8, -8, 9, -9, 10, -11, 12]
    array = [10, -3, -4, 7, 6, 5, -4, -1]
    print(minAdjDiff(array))