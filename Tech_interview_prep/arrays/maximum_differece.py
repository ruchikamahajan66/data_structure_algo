def max_diff(arr):
    res = arr[1] - arr[0]
    min_value = arr[0]
    for j in range(1, len(arr)):
        res = max(res, arr[j]-min_value)
        min_value = min(min_value, arr[j])
    return res


if __name__ == '__main__':
    array = [2,3,10,6,4,8,1]
    print(max_diff(array))