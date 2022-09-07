"""
LEETCODE

Problem: Longest Common Prefix
"""

def find_longest_common_prefix(words):

    # Find the shortest word in order to start the while loop
    lengths = []
    for word in words:
        lengths.append(len(word))

    limit_for_while_loop = min(lengths)

    common_string = ""
    index = 0
    while index < limit_for_while_loop:

        letters = []
        for word in words:
            letters.append(word[index])
        if letters[:] == letters[::-1]:
            common_string += letters[0]
        else:
            break
        index += 1
    return common_string

if __name__ == "__main__":

    array = ["flower", "flow", "flight"]
    print(find_longest_common_prefix(array))
