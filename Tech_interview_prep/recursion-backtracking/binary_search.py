# time complexity = log2(N)
def binary_search(arr, start, end, key):
    if start > end:
        return False
    mid = int((start + end) / 2)
    if arr[mid] == key:
        return True
    if arr[mid] > key:
        return binary_search(arr, start, mid - 1, key)
    else:
        return binary_search(arr, mid + 1, end, key)


def binary_search_iterative_slution(arr, start, end, key):
    while (start <= end):
        mid = int((start + end) / 2)
        present = True

        if arr[mid] == key:
            print(mid)
            break
        if arr[mid] < key:
            start = mid + 1
        else:
            end = mid - 1
        if not present:
            print(-1)


if __name__ == '__main__':
    arr = [2, 5, 8, 16, 20, 23, 30, 35, 41, 63]
    target = 6
    start = 0
    end = len(arr) - 1
    # print(binary_search(arr, start, end, target))
    print(binary_search_iterative_slution(arr, start, end, target))

