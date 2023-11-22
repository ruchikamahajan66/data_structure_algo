from cmath import sqrt


def roots(a, b, c):
    d = sqrt(b*b - 4 * a * c).real
    if d < 0:
        return
    else:
        root1 = (-b + d) / (2 * a)
        root2 = (-b -d) / (2 * a)
    return int(root1), int(root2) if root1 > root2 else root2

def roots_1(a, b, c):
    import math

    d = b ** 2 - 4 * a * c

    if d < 0:
        return [-1]
    else:
        x1 = (-b + d ** 0.5) / (2 * a)
        x2 = (-b - d ** 0.5) / (2 * a)

    if x1 >= x2:
        return [math.floor(x1), math.floor(x2)]
    else:
        return [math.floor(x2), math.floor(x1)]


if __name__ == '__main__':
    a = 752
    b = 904
    c = 164
    print(roots_1(a, b, c))
