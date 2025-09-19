def frequency(arr):
    output = []
    for i in range(1, len(arr) + 1):
        count = 0
        for j in range(0, len(arr)):
            if i == arr[j]:
                count = count + 1
        output.append(count)
    return output


def frequency_optimization(arr):
    ###with hASH MAP
    map = {}
    res = []
    for i in range(0, len(arr)):
        if arr[i] not in map:
            map[arr[i]] = 1
        else:
            map[arr[i]] = map[arr[i]] + 1
    for i in range(0, len(arr)):
        if i+1 not in map:
            res.append(0)
        else:
            res.append(map[i+1])
    return res


if __name__ == '__main__':
    array = [2, 3, 2, 3, 5]
    array = [2, 1, 1]

    # print(frequency(array))
    print(frequency_optimization(array))
