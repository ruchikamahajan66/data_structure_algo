from math import sqrt


def prime_factors(n):
    if n <= 1:
        return
    while n % 2 == 0:
        print(2)
        n = n / 2

    while n % 3 == 0:
        print(3)
        n = n / 3

    bound = int(sqrt(n))
    for i in range(5, bound):
        i = i + 6
        while n % i == 0:
            print(i)
            n = n / i
        while n % i + 2 == 0:
            print(i + 2)
            n = n / (i + 2)
    if n > 3:
        print(int(n))


if __name__ == '__main__':
    number = 450
    print("prime factors are ", prime_factors(number))
