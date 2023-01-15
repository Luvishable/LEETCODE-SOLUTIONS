"""
231. Power of Two

Given an integer n, return true if it is a power of two. Otherwise, return false.

An integer n is a power of two, if there exists an integer x such that n == 2x.

Example 1:

Input: n = 1
Output: true
Explanation: 20 = 1
"""


def is_power_of_two(number):
    flag = False
    while True:
        if number == 1:
            flag = True
            break
        if number % 2 != 0:
            flag = False
            break
        else:
            number = number / 2
            if number == 0:
                flag = True
                break
    return flag

print(is_power_of_two(1024))

