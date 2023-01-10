"""
205. Isomorphic Strings

Given two strings s and t, determine if they are isomorphic.
Two strings s and t are isomorphic if the characters in s can be replaced to get t.
All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

Example 1:

Input: s = "egg", t = "add"
Output: true
Example 2:

Input: s = "foo", t = "bar"
Output: false
Example 3:

Input: s = "paper", t = "title"
Output: true
"""


def is_isomorphic(s, t):
    sozluk = {}
    for i in range(len(s)):
        if s[i] not in sozluk:
            sozluk[s[i]] = t[i]
        else:
            if t[i] != sozluk[s[i]]:
                return False
    return True


def main():
    cases = [
        {
            "s": "egg",
            "t": "add",
            "answer": True
        },
        {
            "s": "foo",
            "t": "bar",
            "answer": False
        },
        {
            "s": "paper",
            "t": "title",
            "answer": True
        }
    ]
    for case in cases:
        assert is_isomorphic(case['s'], case["t"]) == case["answer"]


if __name__ == '__main__':
    main()


