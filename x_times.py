"""
NOT: Bu soru bir akadaşıma İş Bankasının mülkatında soruldu.

1- 8 rakamı 11 defa geçiyor:
key:8 value 11
move: remove 3 times

2- 8 rakamı 17 defa geçiyor
key:8 value 17
move: remove 9 times

3- 8 rakamı 6 defa geçiyor
key:8 value 6
insert 2 times

4- 8 rakamı 3 defa geçiyor
key:8 value 3
remove 3 times

5- 8 rakamı 4 defa geçiyor
key:8 value 4
remove/insert 4 times

"""


"""
eğer rakamın(key'in) value'su key/2 ile key arasında bir değer ise counter'ı key-value kadar artır
eğer rakamın(key'in) value'su key/2'den küçükse counter'ı value kadar artır
eğer rakamın(key'in) value'su key'den büyükse counter'ı value-key kadar artır

key/2 <= value < key =>  counter += (key-value)         CHECKED
value < key/2 => counter += value                       CHECKED
value > key => counter += (value- key)                  CHECKED .
key == value => continue                                CHECKED .
"""

import math

def xTimes(array):
    my_dict = {}
    for i in array:
        if i not in my_dict:
            my_dict[i] = 1
        else:
            my_dict[i] += 1

    counter = 0
    for key, value in my_dict.items():
        if key == value:
            continue

        if math.ceil(key/2) <= value and key > value:
            counter += (key - value)

        if value > key:
            counter += (value - key)

        if value < math.ceil(key/2):
            counter += value

    return counter


if __name__ == '__main__':
    print(xTimes([1, 2, 2, 2, 5, 5, 5, 8]))
