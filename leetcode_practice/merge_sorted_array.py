import numpy as np


def approach1_merge(nums1, m, nums2, n):
    temp = []
    for i in range(0, m):
        temp.append(nums1[i])
    for i in range(0, n):
        temp.append(nums2[i])
    temp.sort()
    for i in range(0, m + n):
        nums1[i] = temp[i]
    print(nums1)


def approach2_merge(nums1, m, nums2, n):
    for i in range(m, len(nums1)):
        nums1[i] = nums2[i - m]
    nums1.sort()
    print(nums1)


def approach3_merge(nums1, m, nums2, n):
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


def sum_of_two_list(test_list1, test_list2):
    # printing original lists
    print("Original list 1 : " + str(test_list1))
    print("Original list 2 : " + str(test_list2))

    # using numpy.sum() to add two lists
    res_array = np.array(test_list1) + np.array(test_list2)
    res_list = res_array.tolist()

    # printing resultant list
    print("Resultant list is : " + str(res_list))


if __name__ == '__main__':
    nums1 = [1, 2, 3, 0, 0, 0]
    nums2 = [2, 5, 6]
    m = 3
    n = 3
    # approach1_merge(nums1, m, nums2, n)
    # approach2_merge(nums1, m, nums2, n)
    # approach3_merge(nums1, m, nums2, n)
    test_list1 = [1, 3, 4, 6, 8]
    test_list2 = [4, 5, 6, 2, 10]
    sum_of_two_list(test_list1, test_list2)
