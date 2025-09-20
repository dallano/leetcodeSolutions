# Solution to problem 3136. Valid Word
# A word is considered valid if:

# It contains a minimum of 3 characters.
# It contains only digits (0-9), and English letters (uppercase and lowercase).
# It includes at least one vowel.
# It includes at least one consonant.
# You are given a string word.

# Return true if word is valid, otherwise, return false.

# Notes:

# 'a', 'e', 'i', 'o', 'u', and their uppercases are vowels.
# A consonant is an English letter that is not a vowel.

import re

def isValid(word):
    regex = r"(?i)(?=.*[b-df-hj-np-tv-z])(?=.*[aeiou])^[a-z0-9]{3,}$"
    return re.search(regex, word) is not None

# Test cases
word1 = "234Adas"
word2 = "b3"
word3 = "a3$e"

print(isValid(word3))