"""
29. Divide Two Integers
Medium

Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.

The integer division should truncate toward zero, which means losing its fractional part. For example, 8.345 would be
truncated to 8, and -2.7335 would be truncated to -2.

Return the quotient after dividing dividend by divisor.

Note: Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range:
[−231, 231 − 1]. For this problem, if the quotient is strictly greater than 2**31 - 1, then return 2**31 - 1,
and if the quotient is strictly less than -231, then return -231.

Example 1:

Input: dividend = 10, divisor = 3
Output: 3
Explanation: 10/3 = 3.33333.. which is truncated to 3
"""


def divide_two_integers(dividend, divisor):
    # Firstly, specify the sign of the resultant number
    sign_of_resultant = 1
    if (dividend >= 0 and divisor < 0) or (dividend < 0 and divisor >= 0):
        sign_of_resultant = -1
    dividend = abs(dividend)
    divisor = abs(divisor)
    start = 0
    result = -1 # in order not to include the starter positon which in our case 0.
    while start < dividend:
        start += divisor
        result += 1
    possible_greatest_answer = 2**31
    possible_lowest_answer = -2**31
    if sign_of_resultant == -1:
        return max(possible_lowest_answer, result)
    else:
        return min(possible_greatest_answer, result)


if __name__ == '__main__':
    answer = divide_two_integers(10, -3)
    assert answer == 3


