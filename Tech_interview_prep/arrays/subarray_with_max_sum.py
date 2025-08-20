if __name__ == '__main__':
    array = [1, 2,-3, 4, 5]
    curr = 0
    maxi = float("-inf")
    max_subarray = []
    for i in range (0, len(array)):
        if array[i] < 0:
            max_subarray = []
            print("subarray with max sum is ", -1)
        curr =  curr + array[i]
        if curr > maxi:
            maxi = curr
            max_subarray.append(i+1)
    print("subarray with max sum is ", max_subarray)



