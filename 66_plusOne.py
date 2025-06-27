# Solution to 66. Plus One
# You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer.
# The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.
# Increment the large integer by one and return the resulting array of digits.

def plusOne(digits):
    newList = []
    s = ""

    for num in digits:
        s = s + str(num) # Convert values into a string
    
    s = str(int(s) + 1) # Convert results of integer addition into string

    for i in range(len(s)):
        newList.append(int(s[i])) # Add integer values of string into a new list

    return newList

nums = [9, 4, 3, 9, 9, 9]
print(plusOne(nums))