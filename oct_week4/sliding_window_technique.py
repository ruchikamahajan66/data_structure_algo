def maximum_sum(arr, k):
    current_sum = 0
    for i in range(0, k):
        current_sum = current_sum + arr[i]
        res = current_sum

    for j in range(k, len(arr)):
        current_sum = current_sum - arr[j - k] + arr[j]
        if current_sum > res:
            res = current_sum
    return res


def naive_maximum_sum(arr, k):
    n = len(arr)
    res = float('-inf')
    for i in range(0, n - k + 1):
        sum = 0
        for j in range(i, i + k):
            sum = sum + arr[j]
            if sum > res:
                res = sum
    return res


if __name__ == '__main__':
    arr = [-1, 2, 4, 6, 3, 3, 7, 32, 0, 9]
    size = 4
    # print(maximum_sum(arr, size))
    print(naive_maximum_sum(arr, size))
