from math import sqrt


def all_divisor(n):
    i = 1
    divisors = []
    while (i * i < n):
        if (n % i == 0):
            print("all divisors are: ", i)
            divisors.append(i)
        i = i + 1

    i = int((sqrt(n)))
    while (i >= 1):
        if n % i == 0 and i != n / i:
            print("all divisors are: ", int(n / i))
            divisors.append(int(n/i))
        i = i - 1
    return divisors


if __name__ == '__main__':
    number = 15
    print("all divisors are: ", all_divisor(number))
