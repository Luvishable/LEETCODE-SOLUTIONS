# SOLUTION 1

"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
"""

def two_sum_1(array, target):

    for i in range(len(array)):
        complementary = target - array[i]
        for j in range(i+1, len(array)):
            if array[j] == complementary:
                return [i,j]







