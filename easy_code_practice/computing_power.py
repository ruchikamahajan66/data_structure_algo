def power(x,n):
    if n == 0:
        return 1
    temp = power(x, int(n/2))
    temp = temp*temp
    if n %2 ==0:
        return temp
    else:
        return temp*x


if __name__ == '__main__':
    x =3
    n = 5
    print(power(x,n))