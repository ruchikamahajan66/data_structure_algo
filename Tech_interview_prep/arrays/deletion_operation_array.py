## In C, you just reduce the array size n and “ignore” the last slot.
### In python (list), len(arr) does not change automatically, so the last element remains in the list.
####in this case we just pop the last element.

def deletion_operation(arr, x):
    for i in range(0, len(arr)):
        if arr[i] == x:
            break
    if i == len(arr):
        return len(arr)
    for j in range(i, len(arr) - 1):
        arr[j] = arr[j + 1]
    arr.pop()
    print(arr)
    return len(arr) - 1


if __name__ == '__main__':
    arr = [3, 8, 12, 5, 6]
    x = 12
    print("length of array is", deletion_operation(arr, x))
