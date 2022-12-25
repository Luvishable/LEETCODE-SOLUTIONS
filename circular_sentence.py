"""
LEETCODE 2490.

Words consist of only uppercase and lowercase English letters. Uppercase and lowercase English letters are considered different.

A sentence is circular if:

The last character of a word is equal to the first character of the next word.
The last character of the last word is equal to the first character of the first word.
For example, "leetcode exercises sound delightful", "eetcode", "leetcode eats soul" are all circular
sentences. However, "Leetcode is cool", "happy Leetcode", "Leetcode" and "I like Leetcode" are not circular sentences.

Given a string sentence, return true if it is circular. Otherwise, return false.

Input: sentence = "leetcode exercises sound delightful"
Output: true
Explanation: The words in sentence are ["leetcode", "exercises", "sound", "delightful"].
- leetcode's last character is equal to exercises's first character.
- exercises's last character is equal to sound's first character.
- sound's last character is equal to delightful's first character.
- delightful's last character is equal to leetcode's first character.
The sentence is circular.

"""

def circular_sentence(sentence):

    words = sentence.split(" ")

    for i in range(len(words)):
        son_harf = words[i][-1]
        ilk_harf = words[(i + 1) % len(words)][0]

        if son_harf != ilk_harf:
            return False
    return True

if __name__ == '__main__':
    print(circular_sentence("leetcode exercises sound delightful"))




























