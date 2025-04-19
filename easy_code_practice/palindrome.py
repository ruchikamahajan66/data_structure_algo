def palindrome(number):
    rev = 0
    temp = number
    while temp!=0:
        ld = temp % 10
        rev = rev * 10 + ld
        temp = temp//10
    return rev==number


if __name__ == '__main__':
    number = 763
    print(palindrome(number))
