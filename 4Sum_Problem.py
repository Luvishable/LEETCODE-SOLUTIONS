"""
Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]]
such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order
"""

def fourSum(array_A, array_B, array_C, array_D):

    dict = {}
    answer = 0

    for i in range(len(array_A)):
        x = array_A[i]
        for j in range(len(array_B)):
            y = array_B[j]
            if x+y not in dict:
                dict[x + y] = 0
            else:
                dict[x + y] += 1

    for i in range(len(array_C)):
        x = array_C[i]
        for j in range(len(array_D)):
            y = array_D[j]
            target = -(x + y)
            if target in dict:
                answer += 1

    return answer

