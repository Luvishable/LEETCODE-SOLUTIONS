"""
338. Counting Bits

Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's
in the binary representation of i.

Example 1:

Input: n = 2
Output: [0,1,1]
Explanation:
0 --> 0
1 --> 1
2 --> 10
"""


def count_bits(number):
    answer_array = []
    for i in range(0, number + 1):
        binary_rep = ''
        temp_num = i
        while temp_num > 0:
            kalan = temp_num % 2
            bolum = temp_num // 2
            if kalan == 1:
                binary_rep += str(kalan)
            temp_num = bolum
        answer_array.append(len(binary_rep))
    return answer_array

print(count_bits(5))













