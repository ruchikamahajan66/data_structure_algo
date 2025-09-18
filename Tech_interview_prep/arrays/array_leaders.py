def array_leader(arr):
    for i in range(0, len(arr)):
        flag = False
        for j in range(i + 1, len(arr)):
            if arr[i] <= arr[j]:
                flag = True
                break
        if flag == False:
            print(arr[i])


def array_leader_optimized_soln(arr):
    n = len(arr)
    curr_leader = arr[n - 1]
    array_leader = [curr_leader]
    # print(curr_leader)
    for i in range(n - 2, -1, -1):
        if arr[i] > curr_leader:
            curr_leader = arr[i]
            # print(curr_leader)
            array_leader.append(curr_leader)

    for i in range(len(array_leader) - 1, -1, -1):
        print(array_leader[i])
    return array_leader


def array_leader_func(arr):
    # code here
    n = len(arr)
    curr_leader = arr[n - 1]
    array_leader = [curr_leader]
    # print(curr_leader)
    for i in range(n - 2, -1, -1):
        if arr[i] > curr_leader:
            curr_leader = arr[i]
            array_leader.append(curr_leader)

    for i in range(len(array_leader) - 1, -1, -1):
        return array_leader[::-1]


if __name__ == '__main__':
    array = [16, 17, 4, 3, 5, 2]
    # array_leader(array)
    # print(array_leader_optimized_soln(array))
    print(array_leader_func(array))
