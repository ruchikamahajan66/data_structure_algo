def is_palindrome(n):
    rev = 0
    temp = n
    while temp != 0:
        last_digit = temp % 10
        rev = rev * 10 + last_digit
        temp = int(temp / 10)
    if rev == n:
        print("given numer is a palindrome number")
    else:
        print("given numer is not a palindrome number")


if __name__ == '__main__':
    number = 336
    is_palindrome(number)
