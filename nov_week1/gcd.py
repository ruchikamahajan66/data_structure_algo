def min(x, y):
    if x > y:
        min = y
    else:
        min = x
    return min


def naive_gcd(x, y):
    res = min(x, y)
    while res > 0:
        if x % res == 0 and y % res == 0:
            break
        res = res - 1

    return res


def eucledian_algo(a, b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a


def optmized_eucledian_algo(a, b):
    if b == 0:
        return a
    else:
        return optmized_eucledian_algo(b, a % b)


if __name__ == '__main__':
    x = 10
    y = 15
    # print(min(x,y))
    # print(naive_gcd(x, y))
    # print(eucledian_algo(x, y))
    print(optmized_eucledian_algo(x,y))
