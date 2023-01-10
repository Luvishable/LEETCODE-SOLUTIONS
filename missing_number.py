"""
Write a function to find the missing number in a given integer array of 1 to 100.
"""


def missing_number(array):
    for i in range(len(array)):
        if array[i + 1] - array[i] > 1:
            return array[i + 1] - 1

        
if __name__ == '__main__':
    print(missing_number([1, 2, 3, 4, 6]))