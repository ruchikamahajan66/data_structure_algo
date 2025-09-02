# naive approach
def rm_Dups(arr):
    temp = []
    temp.append(arr[0])
    res = 1
    for i in range(1, len(arr)):
        if temp[res - 1] != arr[i]:
            temp.append(arr[i])
            res = res + 1

    for i in range(0, res):
        arr[:] = temp[:res]
        return res

def eff_soln(arr):
    res =1

    for i in range (1, len(arr)):
        if arr[i] != arr[res-1]:
            arr[res] = arr[i]
            res =  res+1
    return res


if __name__ == '__main__':
    array = [10, 20, 20, 30, 30, 30]
    # print(rm_Dups(array))
    print(eff_soln(array))
