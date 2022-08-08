# Verilen bir arrayde k adet elemanı frequency'si en çok olandan en az olana doğru sırala

# Ornegin:
# input:      array = [5,3,3,2,8,8,6,6,8,8,5,5,1], k = 2 olsun
# output:     8 5
# çünkü 8 elemanının frekansı 4, 5 elemanının frekansı 3. Outputta bu elemanlar azalan şekilde sıralanmalı

def k_elements_with_frequency(array, k):

    # bir sözlük içerisinde elemanları frekansları ile beraber depola
    my_dict = {}

    # for dongusu ile array icerisinde dolas ve eleman-frekans iliskisini sözlük içinde depola
    for i in range(len(array)):
        if array[i] not in my_dict:
            my_dict[array[i]] = 1
        else:
            my_dict[array[i]] += 1

    # sözlük value'lerini azalan şekilde sırala
    sorted_ = sorted(my_dict.items(), key=lambda x: x[1], reverse=True)

    # sadece elemanları içeren bir liste yarat
    only_values = [i[0] for i in sorted_]

    # istenilen k adet elemeanı döndür
    return only_values[:k]


# Deneme:

array = [5, 3, 3, 2, 8, 8, 6, 6, 8, 8, 5, 5, 1]
k = 2
print(k_elements_with_frequency(array, k))




