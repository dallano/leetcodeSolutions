# Solution to 2016. Maximum Difference Between Increasing Elements
# Given a 0-indexed integer array nums of size n, find the maximum difference between nums[i] and nums[j]
# (i.e., nums[j] - nums[i]), such that 0 <= i < j < n and nums[i] < nums[j].
# Return the maximum difference. If no such i and j exists, return -1.

def maximumDifference(nums):
    maxDifference = -1

    for i in range(len(nums)):
        for j in nums[i:]:
            if j > nums[i] and j - nums[i] > maxDifference:
                maxDifference = j - nums[i]

    return maxDifference

# Test cases:
nums1 = [7, 1, 5, 4] # Solution 4
nums2 = [9, 4, 3, 2] # Solution -1
nums3 = [1, 5, 2, 10] # Solution 9

print(maximumDifference(nums3))