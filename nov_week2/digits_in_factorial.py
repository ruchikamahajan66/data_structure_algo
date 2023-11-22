def digitsInFactorial(N):
    # code here
    fact = 1
    for i in range(1, N + 1):
        fact = fact * i

    digits = 0
    while fact > 0:
        fact = int(fact / 10)
        digits = digits + 1
    return digits


if __name__ == '__main__':
    N =7
    print(digitsInFactorial(N))
