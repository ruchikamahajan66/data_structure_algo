def moveToEnd(arr):
    for i in range(0, len(arr)):
        if arr[i] == 0:
            for j in range(i + 1, len(arr)):
                if arr[j] != 0:
                    temp = arr[i]
                    arr[i] = arr[j]
                    arr[j] = temp

    print("new array is", arr)
    return arr


def eff_soln(arr):
    count = 0
    for i in range(0, len(arr)):
        if arr[i] != 0:
            temp = arr[count]
            arr[count] = arr[i]
            arr[i] = temp
            count = count + 1
    return arr


if __name__ == '__main__':
    arr1 = [8, 5, 0, 10, 0, 20]
    arr2 = [0, 0, 0, 10, 0]
    arr3 = [10, 20]

    # print(moveToEnd(arr3))
    print(eff_soln(arr3))
