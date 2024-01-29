"""
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.



Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
Example 2:

Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation:
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]


Constraints:

1 <= nums.length <= 105
-231 <= nums[i] <= 231 - 1
0 <= k <= 105


Follow up:

Try to come up with as many solutions as you can. There are at least three different ways to solve this problem.
Could you do it in-place with O(1) extra space?
"""


def rotate_easy_approach(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    rotated_array = []
    for i in range(0, len(nums)):
        rotated_array.append(nums[-k])
        k = k - 1
    for i in range(0, len(nums)):
        nums[i] = rotated_array[i]
    return nums


def rotate_medium_approach(nums, k):
    n = len(nums)
    rotated_array = []
    for i in range(0, n):
        rotated_array.append(nums[i])
    for i in range(0, n):
        nums[(i + k) % n] = rotated_array[i]
    return nums


def reverse(nums, i, j):
    while (i < j):
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp
        i = i + 1
        j = j - 1


def rotate_hard_approach(nums, k):
    reverse(nums, 0, len(nums) - k - 1)
    reverse(nums, len(nums) - k, len(nums) - 1)
    reverse(nums, 0, len(nums) - 1)
    return nums


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    print(rotate_easy_approach(nums, k))
    print(rotate_medium_approach(nums, k))
    print(rotate_hard_approach(nums, k))
