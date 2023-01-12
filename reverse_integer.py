"""7. Reverse Integer
Medium

Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the
signed 32-bit integer range [-231, 231 - 1], then return 0.
Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21
"""


def reverse_integer(number):
    length_of_number = len(str(number))
    reversed_number = ""
    for power in range(length_of_number - 1, -1, -1):
        digit = number // (10 ** power)
        if digit == 0:
            number = number % (10 ** power)
            continue
        reversed_number += str(digit)
        number = number % (10 ** power)
    return int(reversed_number[::-1])

print(reverse_integer(120))





