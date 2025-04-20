"""
Determine the factorial of a given number where number is greater than zero
"""


"""
iterative solution
with time complexity = O(n)
"""


def factorial_of_a_number(num, fact):
    for i in range(2, num + 1):
        fact = fact * i
    return fact


"""
iterative solution
with time complexity = O(n)
"""


def factorial_of_a_number_recurssion(num, fact):
    for i in range(2, num + 1):
        fact = fact * i
    return fact


if __name__ == '__main__':
    number = 3
    fact = 1
    print("iterative factorial is ",factorial_of_a_number(number, fact))
    print("recursive factorial is ",factorial_of_a_number_recurssion(number, fact))
