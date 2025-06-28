# Solution to 3151. Special Array
# An array is considered special if the parity of every pair of adjacent elements is different. In other words,
# one element in each pair must be even, and the other must be odd.
# You are given an array of integers nums. Return true if nums is a special array, otherwise, return false.

def isArraySpecial(nums):
    if len(nums) == 0:
        return True

    prevEven = True if nums[0] % 2 == 0 else False

    for i in range(1, len(nums)):
        if (prevEven and nums[i] % 2 == 0) or (not prevEven and nums[i] % 2 == 1):
            return False

        prevEven = not prevEven

    return True

# Test cases:
nums1 = [1] #True
nums2 = [2, 1, 4] #True
nums3 = [4, 3, 1, 6] #False

nums4 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1] # False
nums5 = [1, 2, 3, 4, 5, 3, 6, 7, 8, 9] # False
nums6 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0] # True

print(isArraySpecial(nums2))