def oneplus(digits):
    newdigits = []
    result = []
    carry = 1
    for i in range(len(digits) - 1, -1, -1):
        sum = digits[i] + carry
        num = sum % 10
        carry = int(sum / 10)
        newdigits.append(num)
    if carry == 1:
        newdigits.append(carry)
    for i in range(0, len(newdigits)):
        result.append(newdigits[len(newdigits)-1-i])
    return result


if __name__ == '__main__':
    digits = [9,9,9,9]
    print(oneplus(digits))
