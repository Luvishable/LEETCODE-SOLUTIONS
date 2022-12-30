"""
1) Kelimenin ortasındaki harfin index'ini bul ve middle değişkenine ata

2) Middle'ın sol ve sağında kalan harfleri dolaş

3) Eğer harfler birbirinin aynıysa return true
"""

def is_palindrome(word):
    middle = len(word) // 2
    left = middle - 1
    right = middle + 1
    for i in range(middle):
        if word[left] == word[right]:
            left = left - 1
            right = right + 1
        else:
            return False
        return True

