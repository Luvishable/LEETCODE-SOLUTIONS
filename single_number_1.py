"""Verilen bir array'in içerisinde sadece 1 adet bulunan sayıyı ekrana yazdır"""


def single_number(array):
    my_dict = {}
    for number in array:
        if number in my_dict:
            my_dict[number] += 1
        else:
            my_dict[number] = 1
    for key, value in my_dict.items():
        if my_dict[key] == 1:
            print(key)
            break
single_number([1,1,2,2,3,4,4])

