# 100,4,200,2,3,1
# {
# 	100: 1,
# 	200:1,
# 	1:1+1+2
# }
# Map/dict
# O(1) --> present
# list
# O(n) --> present
#
# map[arr[i]+1]
# loop condition --> 101, 102, 103, 104, 105
# start = 101
# count = 0
# while(start in map):
#    start = start +1
#    count = count+1;
#
# if start in map:
# 100, 101, 4, 200, 2, 3, 1
def longestConsecutive(nums):
    map = {}
    max_so_far = 0
    if len(nums) == 0:
        return 0
    for i in range(0, len(nums)):
        map[nums[i]] = 1
    print(map)
    for i in range(0, len(nums)):
        start = nums[i] + 1
        while start in map:
            map[nums[i]] = map[nums[i]] + map[start]
            map.pop(start)
            start = start + 1
    print(map)
    for key, value in map.items():
        if max_so_far < value:
            max_so_far = value

    return max_so_far


if __name__ == '__main__':
    # nums = [100, 4, 200, 1, 3, 2]
    nums =  [1, 0, -1]
    print(longestConsecutive(nums))
