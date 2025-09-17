def soln1(arr):
    maximum = arr[0]
    second_maximum = -1
    for i in range(0, len(arr)):
        if arr[i] > maximum:
            maximum = arr[i]

    for i in range(0, len(arr)):
        if arr[i] > second_maximum and arr[i] != maximum:
            second_maximum = arr[i]
    return [maximum, second_maximum]


if __name__ == '__main__':
    array = [2, 1, 2,3,6,3,8,9,0,-1,-2,10]
    print(soln1(array))
