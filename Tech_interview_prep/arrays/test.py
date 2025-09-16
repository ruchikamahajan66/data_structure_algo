def insertAtIndex( arr, index, val):
    # i =0
    # newarray = []
    # while i <= len(arr):
    #     if i < index:
    #         newarray.append(arr[i])
    #     elif i == index:
    #         newarray.append(val)
    #     else:
    #         newarray.append(arr[i-1])
    #     i = i+1
    # return newarray
    i = 0
    new_array = []
    while i <= len(arr):
        if i < index:
            new_array.append(arr[i])
        elif i == index:
            new_array.append(val)
        else:
            new_array.append(arr[i - 1])
        i = i+1
    return new_array


def sol2():
    # code here
    if index > len(arr):
        arr.append(val)
    else:
        arr[index] = val
        return arr


if __name__ == '__main__':
    arr = [1,2 ,3, 4, 5]
    index = 2
    val = 90
    print("original array is", arr)
    print(insertAtIndex(arr, index, val))
