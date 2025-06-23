# Solution to 5. Longest Palindromic String ( Brute Force: O(n^2) time)

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

string = "ccc1112321 454"
print(longestPalindrome(string))
