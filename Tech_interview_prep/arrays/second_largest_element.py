

def getSecondLargest(arr):
    second_max_index = -1
    max_so_far = float('-inf')
    second_max_so_far = float('-inf')
    for i in range (0, len(arr)):
        if arr[i]> max_so_far:
            max_so_far = arr[i]
            max_index = i
    for j in range (0, len(arr)):
        if arr[j] == max_so_far:
            continue
        if arr[j]> second_max_so_far:
            second_max_so_far = arr[j]
            second_max_index = j+1
    return second_max_index


if __name__ == '__main__':
    arr = [5,20,12,20,10]
    arr = [10,10, 10]
    print(getSecondLargest(arr))

