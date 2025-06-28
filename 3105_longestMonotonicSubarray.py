# Solution to... 3105. Longest Strictly Increasing or Strictly Decreasing Subarray
# You are given an array of integers nums. Return the length of the longest subarray of nums which is either strictly increasing or strictly decreasing.

def longestMonotonicSubarray(nums):
    longest = 1
    ascentCount  = 1
    descentCount = 1

    if len(nums)== 0:
        return 0

    for i in range(1, len(nums)):
        if nums[i] > nums[i - 1]:
            descentCount = 1
            ascentCount += 1
            if ascentCount > longest:
                longest = ascentCount

        elif nums[i] < nums[i - 1]:
            ascentCount = 1
            descentCount += 1
            if descentCount > longest:
                longest = descentCount

        else:
            ascentCount, descentCount = 1, 1

    return longest

# Test cases:
nums1 = [1, 4, 3, 3, 2] # Solution: 2
nums2 = [3, 3, 3, 3] # Solution: 1
nums3 = [3, 2, 1] # Solution: 3
nums4 = [1, 2, 3, 4, 4, 4, 4, 4, 5, 6, 7, 8] # Solution 5
nums5 = [1, 9, 7, 1]

print(longestMonotonicSubarray(nums5))