def iteractive_fact(n):
    res = 1
    for i in range(1, n + 1):
        res = res * i
    return res


def rec_fact(n):
    if n == 0:
        return 1
    return n * rec_fact(n - 1)


if __name__ == '__main__':
    number = 251
    # print(fact(number))
    print(rec_fact(number))
