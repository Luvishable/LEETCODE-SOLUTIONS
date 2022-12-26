"""
1399. Count Largest Group

You are given an integer n.

Each number from 1 to n is grouped according to the sum of its digits.
Return the number of groups that have the largest size.

Example 1:

Input: n = 13
Output: 4
Explanation: There are 9 groups in total, they are grouped according sum of its digits of numbers from 1 to 13:
[1,10], [2,11], [3,12], [4,13], [5], [6], [7], [8], [9].
There are 4 groups with largest size.

Example 2:

Input: n = 2
Output: 2
Explanation: There are 2 groups [1], [2] of size 1.
"""

def slice_number(number):
    str_number = str(number)
    length_of_number = len(str_number)

    sum = 0

    for i in range(length_of_number - 1, -1, -1):
        digit = number // (10 ** i)
        number = number % (10 ** i)
        sum += digit
    return sum


def count_largest_group(nums):

    groups_list = []

    for num in nums:

        rakamlar_toplami = slice_number(num)

        if rakamlar_toplami != num:
            if rakamlar_toplami > 9:
                rakamlar_toplami_2 = slice_number(rakamlar_toplami)
                groups_list.append([num, rakamlar_toplami, rakamlar_toplami_2])
            else:
                groups_list.append([num, rakamlar_toplami])

        else:
            groups_list.append([num])

    counter = 0
    for i in range(len(groups_list) - 1, -1, -1):
        if len(groups_list[i]) < len(groups_list[-1]):
            break
        counter += 1
    return counter


if __name__ == '__main__':
    array = [1,2,3,4,5,6,7,8,9,10,11,12,13]
    print(count_largest_group(array))









