# Solution to 3335. Total Characters in string after transformations
# You are given a string s and an integer t, representing the number of transformations to perform. In one transformation,
# every character in s is replaced according to the following rules:
# If the character is 'z', replace it with the string "ab".

# Otherwise, replace it with the next character in the alphabet. For example, 'a' is replaced with 'b', 'b' is replaced with 'c', and so on.
# Return the length of the resulting string after exactly t transformations.
# Since the answer may be very large, return it modulo 10^9 + 7.


def lengthAfterTransformations(s, t):
    intArray = [0] * 26 # Each index represents the count of each digit
    mod = 10 ** 9 + 7

    # Initialize array with count of each letter O(len(s))
    for char in s:
        intArray[ord(char) - ord('a')] += 1

    # This func should run in O(t*n) time where n = 26
    for _ in range(t):
        newIntArray = [0] * 26

        # Setup next array using previous values
        for i in range(25):
            newIntArray[i + 1] += intArray[i]

        # For every z, add 1 'a' and 'b'
        newIntArray[0] += intArray[25] % mod
        newIntArray[1] += intArray[25] % mod

        intArray = newIntArray

    # Return value is the sum of the count of each character we have
    return sum(intArray) % (10 ** 9 + 7)

s1 = "zayz"
t1 = 28
s2 = "ajqktcurgdvlibczdsvnsg"
t2 = 7517
s3 = "wifspsjysmjhyjrivipgfzuwche"
t3 = 9284

print(lengthAfterTransformations(s3, t3))
