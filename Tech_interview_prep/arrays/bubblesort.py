def bubbleSort(arr):
    n =  len(arr)
    for i in range(0, n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] =  temp
    return arr


if __name__ == '__main__':
    array =  [6,0,3,5]
    array = [2,5,6,8,7,9,0,2,3,1]
    print(bubbleSort(array))