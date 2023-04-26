#Function to find a continuous sub-array which adds up to a given number and return Arraylist
def subarray_with_given_sum(arr, s):
    current_sum = 0
    l = 0
    r = 0
    n = len(array)
    res = []
    for i in range(0,n):
        current_sum = current_sum +arr[i]
        r = i
        while(current_sum>s):
            current_sum = current_sum - arr[l]
            l = l+1
            if(l>r):
                r = l
        if current_sum==sum and current_sum!=0:
            res.append(l+1)
            res.append(r+1)
            return res

    res.append(-1)
    return res





if __name__ == '__main__':
    array =  [1, 2, 3, 7, 5]
    sum = 12
    print(subarray_with_given_sum(array,sum))
