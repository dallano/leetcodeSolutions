# Solution to 5. Longest Palindromic String ( Brute Force: O(n^2) time)
# Given a string s, return the longest palindromic substring in s.

def longestPalindrome(s):
    longestPalindrome = ""
    max = 0

    if len(s) < 1:
        return ""

    for i in range(len(s)):
        for y in range(i, len(s)):
            substring = s[i:y + 1]
            length = len(substring)

            if length > max and substring == substring[::-1]:
                max = length
                longestPalindrome = substring

    return longestPalindrome

# Test cases:
string = "ccc1112321 454"
print(longestPalindrome(string))
