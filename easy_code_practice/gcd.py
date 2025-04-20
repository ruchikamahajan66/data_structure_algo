def gcd(a, b):
    if a == 0 and b == 0:
        return None
    if a < b:
        res = a
    else:
        res = b

    while (res > 0):
        if a % res == 0 and b % res == 0:
            break
        res = res - 1
    return res
def eucledian_algo(a,b):
    while(a!=b):
        if b<a:
            a= a-b
        else:
            b = b-a

    return a


if __name__ == '__main__':
    a = 0
    b = 0
    # print("gcd of two numbers are ", gcd(a, b))
    print("gcd of two numbers are ", eucledian_algo(a,b))
