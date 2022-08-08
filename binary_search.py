# Binary search algoritmasını uygularken left ve right olmak üzere iki adet pointer kullanırız.
# Eğer bizim aradığımız element middle'a denk geliyorsa middle'ı döndürürüz
# Eğer aradığımız element middle'da bulunan elementten küçükse right pointer'ı middle'a eşitliyoruz
# Eğer aradığımız element middle'dan büyükse left pointer'ı middle'a eşitliyoruz

def binarySearch(array, target):

    left = 0
    right = len(array)


    while (left <= right):

        middle = (left + right) // 2
        if (array[middle] == target):
            return middle
        elif (array[middle] < target):
            left = middle + 1
        else:
            right = middle - 1

    return -1

myArray = [1,2,3,4,5,6,7,8,9]
target = 4
resultant_index = binarySearch(myArray, target)

if resultant_index != -1:
    print(f"The target is at the index of {resultant_index}")
else:
    print("The target is not present in the array")


