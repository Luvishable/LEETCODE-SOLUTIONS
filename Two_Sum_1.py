# SOLUTION 1
def two_sum_1(array, target):

    for i in range(len(array)):
        complementary = target - array[i]
        for j in range(i+1, len(array)):
            if array[j] == complementary:
                return [i,j]







