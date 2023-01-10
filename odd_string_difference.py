"""
2451. Odd String Difference

You are given an array of equal-length strings words. Assume that the length of each string is n.

Each string words[i] can be converted into a difference integer array difference[i] of length n - 1
where difference[i][j] = words[i][j+1] - words[i][j] where 0 <= j <= n - 2. Note that the difference between
two letters is the difference between their positions in the alphabet i.e. the position of 'a' is 0, 'b' is 1, and 'z' is 25.

For example, for the string "acb", the difference integer array is [2 - 0, 1 - 2] = [2, -1].
All the strings in words have the same difference integer array, except one. You should find that string.

Return the string in words that has different difference integer array.

Example 1:

Input: words = ["adc","wzy","abc"]
Output: "abc"
Explanation:
- The difference integer array of "adc" is [3 - 0, 2 - 3] = [3, -1].
- The difference integer array of "wzy" is [25 - 22, 24 - 25]= [3, -1].
- The difference integer array of "abc" is [1 - 0, 2 - 1] = [1, 1].
The odd array out is [1, 1], so we return the corresponding string, "abc".
"""

import string

alphabet = list(string.ascii_lowercase)
values = [i for i in range(len(alphabet))]
myDict = {k: v for (k, v) in zip(alphabet, values)}


def odd_string_difference(words):
    length_of_word = len(words[0])
    global_difference = []
    answer = 0
    for i in range(len(words)):
        local_difference = []
        for j in range(0, length_of_word - 1):
            difference = myDict[words[i][j + 1]] - myDict[words[i][j]]
            local_difference.append(difference)
        if local_difference not in global_difference and len(global_difference) > 0:
            answer = words[i]
            global_difference.append(local_difference)
        else:
            global_difference.append(local_difference)
    return answer



print(odd_string_difference(["adc","wzy","abc"]))



















