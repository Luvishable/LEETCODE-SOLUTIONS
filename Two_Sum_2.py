# SOLUTION 2
def two_sum_2(array, target):
    sozluk = {}
    for i in range(len(array)):
        sozluk[i] = target- array[i]
        if array[i] in sozluk.values():
            return reversed[i,array.index(target - array[i])]