# s = "123+(1+(4+5+2)-3)+(6+8)"
# (----- - / + (----- + / - (----))) + () -
def calculator(s):
    sum = 0
    sign = 1
    stack = []
    i = 0
    while i<len(s):
        if s[i]>= '0' and s[i]<= '9':
            num = 0
            while(i < len(s) and  s[i]>= '0' and s[i]<= '9'):
                num = num*10+int(s[i])
                i = i+1
            i=i-1
            sum = sum + sign * num
        elif s[i]=='+':
            sign = 1
        elif s[i]=='-':
            sign = -1
        elif s[i] == '(':
            stack.append(sum)
            stack.append(sign)
            sum =0
            sign = 1
        elif s[i]==')':
            tempSign = stack.pop()
            tempSum = stack.pop()
            sum = tempSum + tempSign * sum
        i = i+1
    return sum


if __name__ == '__main__':
    s = "(1+(4+5+2)-3)+(6+8)"
    # s = "2147483647"
    print(calculator(s))