"""
2206. Divide Array Into Equal Pairs

You are given an integer array nums consisting of 2 * n integers.

You need to divide nums into n pairs such that:

Each element belongs to exactly one pair.
The elements present in a pair are equal.
Return true if nums can be divided into n pairs, otherwise return false.
"""

def divide_into_equal_parts(array):

    my_dict = {}

    for i in range(len(array)):
        if array[i] not in my_dict:
            my_dict[array[i]] = 1
        else:
            my_dict[array[i]] += 1

    for key, value in my_dict.items():
        if value % 2 != 0:
            return False
    return True

if __name__ == '__main__':
    print(divide_into_equal_parts([3, 2, 3, 2, 2, 2]))
