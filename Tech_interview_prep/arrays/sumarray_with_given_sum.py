def subarray_sum(arr, sum):
    curr_sum = 0
    s = 0
    for i in range(0, len(arr)):
        curr_sum = curr_sum + arr[i]
        while sum < curr_sum:
            curr_sum = curr_sum - arr[s]
            s = s + 1
        if curr_sum == sum:
            return True
    return False


def subarray_sum_count(arr, sum):
    curr_sum = 0
    s = 0
    count = 0
    for i in range(0, len(arr)):
        curr_sum = curr_sum + arr[i]
        while sum < curr_sum:
            curr_sum = curr_sum - arr[s]
            s = s + 1
        if curr_sum == sum:
            count = count + 1
    return count


if __name__ == '__main__':
    array = [4, 8, 12, 5, 12, 18]
    sum = 17
    print(subarray_sum(array, sum))
    print(subarray_sum_count(array, sum))
