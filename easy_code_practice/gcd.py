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

def eucledian_optimized_algo(a,b):
    if b ==0:
        return a
    else:
        return eucledian_optimized_algo(b , a%b)




if __name__ == '__main__':
    a = 4
    b = 6
    # print("gcd of two numbers are ", gcd(a, b))
    # print("gcd of two numbers are ", eucledian_algo(a,b))
    print("gcd of two numbers are ", eucledian_optimized_algo(a, b))
