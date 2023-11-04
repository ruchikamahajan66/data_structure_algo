def naive_min_size_subarr_sum(arr, target_sum):
    n = len(arr)
    min_size_of_subarray = float('inf')
    for i in range(0, n):
        sum = arr[i]
        if (sum >= target_sum):
            return 1
        for j in range(i + 1, n):
            sum = sum + arr[j]
            if sum >= target_sum:
                curr_length_of_subarray = j - i + 1
                if min_size_of_subarray > curr_length_of_subarray:
                    min_size_of_subarray = curr_length_of_subarray
    if min_size_of_subarray == float("inf"):
        return 0

    return min_size_of_subarray


def min_size_subarr_sum(arr, target_sum):
    left_pointer = 0
    total_sum = 0
    res = float("inf")
    for right_pointer in range(0, len(arr)):
        total_sum = total_sum + arr[right_pointer]
        while (total_sum >= target_sum):
            total_sum = total_sum - arr[left_pointer]
            window_size = right_pointer - left_pointer + 1
            if res > window_size:
                res = window_size
            left_pointer = left_pointer + 1
    if res == float("inf"):
        return 0

    return res


if __name__ == '__main__':
    arr = [-1, 2, 4, 6, 3, 3, 7, 32, 0, 9]
    sub_arr = [5, 1, 3, 5, 10, 7, 4, 9, 2, 8]
    size = 4
    target_sum = 15
    print(naive_min_size_subarr_sum(sub_arr, target_sum))
    print(min_size_subarr_sum(sub_arr, target_sum))
