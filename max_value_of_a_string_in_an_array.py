"""
Leetcode 2496.

Maximum Value of a String in an Array

The value of an alphanumeric string can be defined as:

The numeric representation of the string in base 10, if it comprises of digits only.
The length of the string, otherwise.
Given an array strs of alphanumeric strings, return the maximum value of any string in strs.



Example 1:

Input: strs = ["alic3","bob","3","4","00000"]
Output: 5
Explanation:
- "alic3" consists of both letters and digits, so its value is its length, i.e. 5.
- "bob" consists only of letters, so its value is also its length, i.e. 3.
- "3" consists only of digits, so its value is its numeric equivalent, i.e. 3.
- "4" also consists only of digits, so its value is 4.
- "00000" consists only of digits, so its value is 0.
Hence, the maximum value is 5, of "alic3".
"""

def max_value_of_string(array):

    max_value = len(array[0])

    for eleman in array:

        if eleman.isdigit() == False:
            value = len(eleman)

        else:
            value = int(eleman)

        if max_value < value:
            max_value = value

    return max_value


if __name__ == '__main__':
    print(max_value_of_string(["alic3", "bob", "3", "4", "00000"]))











