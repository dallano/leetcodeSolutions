# Submitted solution to problem 2311. Longest Binary Subsequence Less Than or Equal to K
# You are given a binary string s and a positive integer k.
# Return the length of the longest subsequence of s that makes up a binary number less than or equal to k.

# Note:
# - The subsequence can contain leading zeroes.
# - The empty string is considered to be equal to 0.
# - A subsequence is a string that can be derived from another string by deleting some or no
#     characters without changing the order of the remaining characters.


# Devnotes:
# As we can delete 1s, we will move from the right side and ignore all 1s s.t. that put our value above k
def longestSubsequence(s, k):
    numOnes  = 0
    decValue = 0
    exponent = 1

    for i, bin in enumerate(s[::-1]):
        if decValue + exponent > k:
            break
        elif bin == '1':
            numOnes += 1
            decValue += exponent
        exponent *= 2

    return s.count('0') + numOnes # Return all 0s, plus amount of 1s we traversed from the right while remaining under k

testS1 = "000000001"
testK1 = 4
testS2 = "1001001110101"
testK2 = 2
testS3 = "1001010" # Leetcode example. Soltion = 5, s.t. k = 5
testK3 = 5
testS4 = "00101001" # Leetcode example. Solution = 6, s.t. k = 1
testK4 = 1

print(longestSubsequence(testS4, testK4))