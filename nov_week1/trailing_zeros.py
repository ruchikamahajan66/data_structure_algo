def naive_soln(n):
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    print(fact)


def efficient_sol(n):
    res = 0
    i = 5
    while i < n+1:
        res = res + int(n / i)
        i = i * 5
    return res


if __name__ == '__main__':
    number = 120
    # naive_soln(number)
    print(efficient_sol(number))
