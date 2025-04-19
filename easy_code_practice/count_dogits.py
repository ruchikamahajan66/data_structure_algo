def count_digits(digit, res):
    while digit > 0:
        digit = digit // 10
        res = res + 1

    print("count digits = ", res)


if __name__ == '__main__':
    digit = 1744489
    res = 0
    count_digits(digit, res)
