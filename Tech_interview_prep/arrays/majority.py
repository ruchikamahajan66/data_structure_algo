def moreFrequent(arr, x, y):
    count_x = 0
    count_y = 0
    for i in range(0, len(arr)):
        if x == arr[i]:
            count_x = count_x + 1
        if y == arr[i]:
            count_y = count_y + 1
    if count_x == count_y:
        return min(x, y)
    if count_x > count_y:
        return x
    else:
        return x


if __name__ == '__main__':
    # array = [1, 1, 2, 2, 3, 3, 4, 4, 4, 4, 5]
    array = [1, 2, 3, 4, 5, 6, 7, 8]
    x = 1
    y = 7
    print(moreFrequent(array, x, y))
