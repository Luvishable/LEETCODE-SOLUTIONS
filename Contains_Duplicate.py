from collections import defaultdict

def contains_duplicate(array):
    sozluk = defaultdict(int)
    for i in array:
        if (sozluk[i]):
            return True
        sozluk[i] += 1
    return False
