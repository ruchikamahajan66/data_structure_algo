def hashing_method(arr):
    # write your code here
    print("hashing")


def MissingNumber_sum_method(arr, n):
    # code here
    print(n)
    array_sum = 0
    sum = (n+1) * ((n+1) + 1) / 2
    for i in range(0, n - 1):
        array_sum = array_sum + arr[i]
        missing_number = sum - array_sum
    return int(missing_number)


def xor_methid(arr):
    print("xor")


if __name__ == '__main__':
    array = [6,1,2,8,3,4,7,10,5]
    n = len(array)
    hashing_method(array)
    MissingNumber_sum_method(array,n)
    xor_methid(array)
