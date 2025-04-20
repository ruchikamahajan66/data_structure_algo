def lcm(a, b):
    res = max(a, b)
    while (True):
        if res % a == 0 and res % b == 0:
            return res
        else:
            res = res + 1


def efficient_soln(a, b):
    if b == 0:
        return a
    else:
        return efficient_soln(b, a % b)


def lcm1_eff(a, b):
    return a * b / efficient_soln(a, b)


if __name__ == '__main__':
    a = 4
    b = 6
    # print(lcm(a, b))
    print(lcm1_eff(a, b))
