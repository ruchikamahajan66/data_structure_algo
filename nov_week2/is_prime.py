from cmath import sqrt


def is_prime_O_n(N):
    if N == 1:
        return False
    for i in range(2, N):
        if N % i == 0:
            return False
    return True


def is_prime_O_sqrt_n(N):
    if N == 1:
        return False
    len = int(sqrt(N).real)
    for i in range(2,len+1):
        if N % i == 0:
            return False
    return True


def is_prime_O_n1(N):
    if N == 1:
        return False
    for i in range(2, N):
        if N % i == 0:
            return False
    return True


if __name__ == '__main__':
    N = 121
    # print(is_prime_O_n(N))
    print(is_prime_O_sqrt_n(N))
