def merge_sorted_array_method1(nums1, nums2, n, m):
    temp = []
    for i in range(0, m):
        temp.append(nums1[i])
    for i in range(0, n):
        temp.append(nums2[i])
    temp.sort()
    print(temp)
    for i in range(0, m + n):
        nums1[i] = temp[i]
    print("nums1 is", nums1)


def merge_sorted_array_method_2(nums1, nums2, m,n):
    for i in range(m, len(nums1)):
        nums1[i] = nums2[i - m]
    nums1.sort()
    return nums1


def merge_sorted_array_method_3(nums1, nums2, n, m):
    p1 = m - 1
    p2 = n - 1
    i = m + n - 1
    while p2 >= 0:
        if p1 >= 0 and nums1[p1] > nums2[p2]:
            nums1[i] = nums1[p1]
            i = i - 1
            p1 = p1 - 1
        else:
            nums1[i] = nums2[p2]
            i = i - 1
            p2 = p2 - 1
    print(nums1)


if __name__ == '__main__':
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    n = 3
    nums2 = [2, 5, 6]

    # merge_sorted_array_method1(nums1, nums2, n, m)
    # print(merge_sorted_array_method_2(nums1, nums2, n, m))
    merge_sorted_array_method_3(nums1, nums2, n, m)
