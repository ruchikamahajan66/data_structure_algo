"""
Naive solution
"""
def isPrime(n):
    # Simple function to check if a number is prime
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False


def primeFactors(n):
    # Function to find and print prime factors
    for i in range(2, n):
        if isPrime(i):
            x = i
            while n % x == 0:
                print(i)
                x = x * i


if __name__ == '__main__':
    number = 12
    print("prime number are", primeFactors(number))
