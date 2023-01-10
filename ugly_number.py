"""
Ugly number is a number whose divisors are only limited to 2,3,5.
"""


def isUgly(number):

    if number <= 0:
        return False
    for prime in [2, 3, 5]:
        while number % prime == 0:
            number = number // prime

    return number == 1