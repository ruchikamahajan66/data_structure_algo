# naive approach (O(n3))
def sum_range(i, j, array):
    res = 0
    for k in range(i, j + 1):
        res = res + array[k]
    return res


def naive_solution(array, max_sum):
    for i in range(0, len(array)):
        for j in range(i, len(array)):
            temp_sum = sum_range(i, j, array)
            if temp_sum > max_sum:
                max_sum = temp_sum
    print("max_sum of subarray is", max_sum)


# better approach (O(n2))
def soln1(array, max_sum):
    for i in range(0, len(array)):
        temp_sum = 0
        for j in range(i, len(array)):
            temp_sum = temp_sum + array[j]
            if temp_sum > max_sum:
                max_sum = temp_sum
    print("max subarray sum is", max_sum)


def sol2(array):
    res = array[0]
    maxEnding = array[0]
    for i in range(1, len(array)):
        maxEnding = max(maxEnding + array[i], array[i])
        res = max(res, maxEnding)
    print("max subarray sum with optimized approach is", res)


def sol3(array):
    curr = 0
    maxi = float('-inf')
    for i in range(0, len(array)):
        curr = curr + array[i]
        if curr > maxi:
            maxi = curr
        if curr < 0:
            curr = 0
    print("max sub array sum is", maxi)


if __name__ == '__main__':
    array = [2, 3, -8, 7, -1, 2, 3]
    max_sum = float('-inf')
    naive_solution(array, max_sum)
    soln1(array, max_sum)
    sol2(array)
    sol3(array)
