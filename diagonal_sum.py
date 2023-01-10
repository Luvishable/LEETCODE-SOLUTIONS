"""
Given 2D list, calculate the sum of diagonal elements
"""

def diagonal_sum(array):
    left_diag = 0
    right_diag = 0
    j = len(array) - 1
    for i in range(len(array)):
        left_diag += array[i][i]
        right_diag += array[i][j]
        j -= 1
    return (left_diag, right_diag)








myList2D = [[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]]


print(diagonal_sum(myList2D))