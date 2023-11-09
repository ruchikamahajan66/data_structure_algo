def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def lcm(a, b):
    lcm = a * b / gcd(a, b)
    return lcm


if __name__ == '__main__':
    x = 4
    y = 6
    print(lcm(x, y))
