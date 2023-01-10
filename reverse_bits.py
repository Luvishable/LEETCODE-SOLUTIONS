"""
Reverse bits of a given 32 bits unsigned integer.

Input: n = 00000010100101000001111010011100
Output:    964176192 (00111001011110000010100101000000)
Explanation: The input binary string 00000010100101000001111010011100 represents the unsigned integer 43261596,
so return 964176192 which its binary representation is 00111001011110000010100101000000.
"""

def reverse_bits(binary_rep):

    length_of_binary = len(binary_rep)
    sum = 0
    for i in range(length_of_binary, -1, -1):
        if int(binary_rep[i]) == 0:
            continue
        sum += int(binary_rep[i]) * 2**((i - length_of_binary) % length_of_binary)
    return sum

sample = '00000010100101000001111010011100'
print(reverse_bits(sample))


