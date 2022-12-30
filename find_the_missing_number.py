"""1'den n'e kadar olan sayılardan oluşan bir array veriliyor. Bu aralıktaki sayılardan biri listede yok.
Bu kayıp sayıyı dönen bir fonksiyon yaz
"""

# 1. çözüm:
# Bu çözümde 1'den n'e kadar olan sayıların toplamını veren formülü kullanabiliriz
# formül: n*(n+1)/2
def find_missing1(array):
    array.sort()
    return int((array[-1] * (array[-1] + 1) / 2) - sum(array))



