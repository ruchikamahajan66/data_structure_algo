from numpy import sort


def mean(arr):
    sum = 0
    for i in range(0, len(arr)):
        sum = sum + arr[i]
    mean = int(sum / len(arr))
    return mean

def median(arr):

    # for i in range(0, len(arr)-1):
    #     if arr[i] > arr[i+1]:
    #         temp = arr[i]
    #         arr[i] = arr[i+1]
    #         arr[i+1] = temp
    sorted_array =  sort(arr)

    if len(sorted_array)%2 ==0:
        median = int((sorted_array[int(len(sorted_array) / 2)] + sorted_array[int(len(sorted_array) / 2) - 1]) / 2)
    else:
        median =  sorted_array[int(len(sorted_array)/2)]
    return median


if __name__ == '__main__':
    arr = [1,2,19,28,5]
    arr = [2,8,4,3]
    # print(mean(arr))
    print(median(arr))