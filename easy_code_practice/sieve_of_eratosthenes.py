def SieveOfEratosthenes(n):
    prime = [True for i in range(n + 1)]
    i = 2
    while i * i <= n:
        if prime[i]:
            for j in range(i * i, n + 1, i):
                prime[j] = False
        i = i + 1
    for i in range(2, n + 1):
        if prime[i]:
            print(i)


if __name__ == '__main__':
    number = 30
    print(SieveOfEratosthenes(number))
