"""
258. Add Digits

Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.
Example 1:

Input: num = 38
Output: 2
Explanation: The process is
38 --> 3 + 8 --> 11
11 --> 1 + 1 --> 2
Since 2 has only one digit, return it.
"""


def add_digit(number):
    if number == 0:
        return 0
    if number == 9:
        return 9
    else:
        return number % 9
