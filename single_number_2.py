def single_number_2(array):

    # Önce verilen array içerisindeki her integer sayinin sadece bir defa bulunduğu bir set oluşturalım
    array_unique_elements = set(array)

    # Bu set'in toplamını iki ile çarparsak array'in orijinalindeki her integer'ın iki defa bulunduğunu varsaymış oluruz
    assumed_sum = 2*sum(array_unique_elements)

    # Eğer assumed_sum'dan orijinal arraydeki integerların toplamını çıkartırsak array içerisinde sadece bir defa
    # bulunan sayıyı bulmuş oluruz
    original_sum = sum(array)

    single_number = assumed_sum - original_sum

    return single_number

def single_number_2_oneLine(array):
    return 2*sum(set(array)) - sum(array)

print(single_number_2_oneLine([1,1,2,3,4,3,2]))
