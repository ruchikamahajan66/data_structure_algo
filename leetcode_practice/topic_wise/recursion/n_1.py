def fun_inc(n):
    if n == 0:
        return
    fun_inc(n - 1)
    print(n)


def fun_dec(n):
    if n == 0:
        return
    print(n)
    fun_dec(n - 1)


if __name__ == '__main__':
    n = 5
    fun_dec(n)
    print("####################")
    fun_inc(n)
