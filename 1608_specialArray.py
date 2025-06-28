# Solution to 1608. Special Array With X Elements Greater than or Equal to X
# You are given an array nums of non-negative integers. nums is considered special if there exists a number x such that there are
# exactly x numbers in nums that are greater than or equal to x.
# Notice that x does not have to be an element in nums.
# Return x if the array is special, otherwise, return -1. It can be proven that if nums is special, the value for x is unique.

# Dev note:
# Reverse the array in sorted order, and use the biggest numbers to find x the quickest
def specialArray(nums):
    nums.sort(reverse=True)

    for i in range(1, len(nums) + 1):
        if nums[i - 1] >= i and (i == len(nums) or nums[i] < i):
            return i

    return -1

# Test cases:
nums1 = [3, 5]
nums2 = [0, 0]
nums3 = [0, 4, 3, 0, 4]

print(specialArray(nums2))