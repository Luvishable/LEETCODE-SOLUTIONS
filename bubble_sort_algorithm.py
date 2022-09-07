def bubble_sort(array):
    for j in range(len(array) - 1):
        second = 1
        for i in range(len(array) - 1):
            if array[second] < array[i]:
                temp = array[i]
                array[i] = array[second]
                array[second] = temp
            second += 1
    return array

if __name__ == "__main__":

    array = [3, 7, 3, 9, 2, 1, 12, 34, 6]
    print(bubble_sort(array))