# Solution to 594. Longest Harmonious Sequence
# We define a harmonious array as an array where the difference between its 
#    maximum value and its minimum value is exactly 1.
# Given an integer array nums, return the length of its longest harmonious 
#   subsequence among all its possible subsequences.

# Dev notes: Turn the array into a dict with a count of each unique value using Counter
#           Iterate through the dict, if our current value + 1 exists, compare their count
#           with the current total max.

def findLHS(nums):
    from collections import Counter
    array = Counter(nums)
    totalMax = 0

    for key in array:
        if key + 1 in array:
            totalMax = max(totalMax, array[key] + array[key + 1])

    return totalMax

# Test Cases
nums1 = [1, 3, 2, 2, 5, 2, 3, 7] # Solution: 5
nums2 = [1, 2, 3, 4] # Solution: 2
nums3 = [1, 1, 1, 1] # Solution: 0

print(findLHS(nums1))