def find_min_max(array):

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

    return [min_number, max_number]

print(find_min_max([101]))