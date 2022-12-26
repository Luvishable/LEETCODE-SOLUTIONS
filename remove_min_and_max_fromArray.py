"""
LEETCODE 2091.

You are given a 0-indexed array of distinct integers nums.

There is an element in nums that has the lowest value and an element that has the highest value. We call them the
minimum and maximum respectively. Your goal is to remove both these elements from the array.

A deletion is defined as either removing an element from the front of the array or removing
an element from the back of the array.

Return the minimum number of deletions it would take to remove both the minimum and maximum element from the array.



Example 1:

Input: nums = [2,10,7,5,4,1,8,6]
Output: 5
Explanation:
The minimum element in the array is nums[5], which is 1.
The maximum element in the array is nums[1], which is 10.
We can remove both the minimum and maximum by removing 2 elements from the front and 3 elements from the back.
This results in 2 + 3 = 5 deletions, which is the minimum number possible.
"""

def remove_min_max(array):

    n = len(array)
    min_number = array[0]
    max_number = array[0]
    j = n - 1

    for i in range(len(array)):

        if i == j:
            break

        current_front = array[i]
        current_back = array[j]

        temp_min = min(current_front, current_back)
        temp_max = max(current_front, current_back)

        if temp_min < min_number:
            min_number = temp_min
        if temp_max > max_number:
            max_number = temp_max

        j -= 1

    indexOf_min_number = array.index(min_number)
    indexOf_max_number = array.index(max_number)

    if indexOf_min_number < n // 2 and indexOf_max_number < n // 2:
        possible_min_move = max(indexOf_min_number, indexOf_max_number) + 1

    elif indexOf_min_number >= n // 2 and indexOf_max_number >= n // 2:
        possible_min_move = n - min(indexOf_min_number, indexOf_max_number)

    else:
        deletion_for_min_number = min(array.index(min_number) + 1, len(array) - array.index(min_number))
        deletion_for_max_number = min(array.index(max_number) + 1, len(array) - array.index(max_number))
        possible_min_move = deletion_for_min_number + deletion_for_max_number

    return possible_min_move

if __name__ == '__main__':

    sample_1 = [2, 10, 7, 5, 4, 1, 8, 6]

    sample_2 = [0, -4, 19, 1, 8, -2, -3, 5]

    sample_3 = [101]

    samples = [sample_1, sample_2, sample_3]

    correct_answers = [5, 3, 1]

    for i in range(len(samples)):
        if remove_min_max(samples[i]) == correct_answers[i]:
            print(f"sample_{i} passed")











