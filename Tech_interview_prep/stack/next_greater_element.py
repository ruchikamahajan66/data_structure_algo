def next_greater_element(arr):
    new_array = []
    stack = []
    for i in range(0, len(arr)):
        new_array.append(-1)
    for i in range(len(arr) - 1, -1, -1):
        while stack and arr[i] >= stack[-1]:
            stack.pop()
        if stack:
            new_array[i] = stack[-1]
        stack.append(arr[i])

    return new_array


if __name__ == '__main__':
    arr =  [1,3,2,4]
    print(next_greater_element(arr))



