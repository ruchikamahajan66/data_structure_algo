#### This will give time complexity of O(n).
def largest_element(array):
    max_so_far = float("-inf")
    max_index = -1
    for i in range(0, len(array)):
        if array[i] > max_so_far:
            max_so_far = array[i]
            max_index = i
    return max_index


#### Can we optimize it to O(1)

if __name__ == '__main__':
    arr = [10, 5, 20, 8]
    print("largest elemnt index is ", largest_element(arr))


