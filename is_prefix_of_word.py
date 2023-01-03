
"""
1455. Check If a Word Occurs As a Prefix of Any Word in a Sentence

Given a sentence that consists of some words separated by a single space, and a searchWord, check if searchWord
is a prefix of any word in sentence.

Return the index of the word in sentence (1-indexed) where searchWord is a prefix of this word. If searchWord is
a prefix of more than one word, return the index of the first word (minimum index). If there is no such word return -1.

A prefix of a string s is any leading contiguous substring of s.

Example 1:

Input: sentence = "i love eating burger", searchWord = "burg"
Output: 4
Explanation: "burg" is prefix of "burger" which is the 4th word in the sentence.
"""


def is_prefix_of_word(sentence, search_word):
    list_of_words = sentence.split(" ")
    for word in list_of_words:
        if word[:len(search_word)] == search_word and len(word) >= len(search_word):
            return list_of_words.index(word) + 1
    return -1


if __name__ == '__main__':
    sentence = "i love eating burger"
    search_word = "burg"
    print(is_prefix_of_word(sentence, search_word))

