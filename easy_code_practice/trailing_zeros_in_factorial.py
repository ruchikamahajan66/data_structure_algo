def trailing_zeros(num):
    fact = 1
    for i in range(1, num + 1):
        fact = fact * i

    res = 0
    while (fact % 10 == 0):  # 120
        res = res + 1
        fact = fact // 10
    return res


def trailing_zeros_efficient_approach(n):
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    res = 0
    i = 5
    while (i <= n):
        res = res + n //  i
        i = i * 5
    return res


if __name__ == '__main__':
    number = 251
    # print("trailing zeros are", trailing_zeros(number))
    print("trailing zeros are", trailing_zeros_efficient_approach(number))
