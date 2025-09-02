## naive approach
def isSorted(array):
    for i in range(0, len(array)):
        for j in range(i + 1, len(array)):
            if arr[j] < arr[i]:
                return False
        return True

def eff_sol(array):
    for i in range(1, len(array)):
        if arr[i] < arr[i-1]:
            return False
    return True

if __name__ == '__main__':
    arr = [7, 20, 0, 50]
    # print(isSorted(arr))
    print(eff_sol(arr))
