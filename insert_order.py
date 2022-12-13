"""
35. Search Insert Position

Given a sorted array of distinct integers and a target value, return the index if the target is found.
If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity
"""


def insert_order(array, target):
    for i in range(len(array)):
        try:
            if array[i] == target:
                return i
            elif array[i] < target and array[i+1] > target:
                return i + 1
        except IndexError:
            return len(array)


my_array = [1, 3, 5, 6]
target = 2
print(insert_order(my_array, target))