# arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# for i in range(0, len(arr)):
#     arr[i] = arr[i] * 2
#
# print(arr)
## Do all the example in pythonic way ....
#******** # example 1 : a = [1, 2, 3, 4]
# a = [x * 2 for x in a]
# do all the question using recursion....\
##############
#Find all the even number between 1 to 10

# for i in range(0, len(arr)):
#     new_array = []
#     if arr[i]%2 ==0:
#         new_array.append(arr[i])
# time complexity = O(n), O(1)

### write down all the sub arrays of this given array

arr = [1,2,3,4]
# subarray of length 1 = (1) (2) (3) (4)
# (1,2), (1,2,3), (1,2,3,4), (2,3), (2,3,4), (3,4)

# Input: arr[] = [1, 2, 3]
# Output: [ [1], [1, 2], [2], [1, 2, 3], [2, 3], [3] ]
#
# Input: arr[] = [1, 2]
# Output: [ [1], [1, 2], [2] ]

##(i,j) = subarray
def subarray(arr):
    subarray = []
    for i in range(0, len(arr)): ## subarray of length 1 = 1
        temp =[]
        for j in range(i, len(arr)):
            temp.append(arr[j])
            subarray.append(temp)
    return subarray


if __name__ == '__main__':
    arr= [1, 2, 3]
    print(subarray(arr))

