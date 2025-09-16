def my_sum(start,end, arr):
    sum =0
    for i in range(start, end+1):
        sum = sum + arr[i]
    return sum


def subarray_sum_equal_k(nums, m):
    count = 0
    sum =0
    for i in range(0, len(nums)):
        for j in range(i, len(nums)):
            sum = my_sum(i, j, nums)
            if sum == m:
                count = count + 1
    return count


if __name__ == '__main__':
    nums = [1,2,3]
    k = 3
    print(subarray_sum_equal_k(nums, k))