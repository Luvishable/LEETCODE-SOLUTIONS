def find_pivot_index(array):

    for i in range(len(array)):
        if sum(array[: i]) == sum(array[i + 1:]):
            return i
    return -1




