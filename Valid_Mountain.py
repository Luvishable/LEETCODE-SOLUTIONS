def validMountain(array):

    if len(array) < 3:
        return False

    i = 1
    while i < len(array) and array[i] > array[i - 1]:
        i += 1

    if i == 1 or i == len(array):
        return False

    while i < len(array) and array[i] < array[i - 1]:
        i += 1

    return i == len(array)