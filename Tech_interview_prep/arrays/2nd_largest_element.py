def second_largest_element(arr):
    largest =  -1
    second_largest = -1
    for i in range(0, len(arr)):
        if arr[i]> largest:
            largest =  arr[i]
    for i in range(0, len(arr)):
        if arr[i]> second_largest and arr[i]!= largest:
            second_largest = arr[i]
    return second_largest


if __name__ == '__main__':
    arr = [12, 35, 1, 10, 34, 35]
    # arr = [10, 10,10]
    print("second largest element in an array is", second_largest_element(arr))
