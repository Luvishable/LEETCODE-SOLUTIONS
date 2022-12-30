# Verilen bir array'de belli bir elemanın ilk ve son bulunduğu index numaralarını döndüren bir fonksiyon yaz

def first_and_last(array, target):
    my_dict = {}
    for i in range(len(array)):
        my_dict[i] = array[i]
    liste = []
    for key,value in my_dict.items():
        if value == target:
            liste.append(key)
    return liste[0],liste[-1]

print(first_and_last([10,11,11,11,12,13,14,14,7,10], 11))
