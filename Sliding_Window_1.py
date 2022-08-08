# Given an array of integers of size N, find maximum sum of K consequtive elements

def maxSum_1(array, windowSize):
    array_size = len(array)
    if array_size < windowSize:
        print("Invalid Operation")
        return -1
    window_sum = sum([array[i] for i in range(windowSize)])
    max_sum = window_sum

    for i in range(array_size - windowSize):
        window_sum = window_sum - array[i] + array[i + windowSize]
        max_sum = max(window_sum, max_sum)

    return max_sum


array = [80, -50, 90, 100, 45, 59, 72, 21, 35, 46, 12]
k = 2
answer = maxSum_1(array, k)
print(answer)