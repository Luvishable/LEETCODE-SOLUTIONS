# artan şekilde sıralanmış ve elemanlarının hepsi birbirinden farklı olan bir arrayde bulunmayanen en küçük sayıyı
# döndüren bir fonksiyon yaz


def find_smallest_misiing_number(array):
    if array[0] != 0:
        return 0
    for i in range(len(array)):
        if i != array[i]:
            return i
