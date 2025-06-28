# Solution to 3011. Can Sort Array
# You are given a 0-indexed array of positive integers nums.
# In one operation, you can swap any two adjacent elements if they have the same number of set bits.
# You are allowed to do this operation any number of times (including zero).
# Return true if you can sort the array in ascending order, else return false.

def canSortArray(nums):
    prevMax = float('-inf')
    currMin = nums[0]
    currMax = nums[0]
    currBits = bin(nums[0])[2:].count('1')

    for i in range(1, len(nums)):
        if currBits == bin(nums[i])[2:].count('1'):
            currMax = max(currMax, nums[i])
            currMin = min(currMin, nums[i])

        else:
            if currMin < prevMax:
                return False

            prevMax = currMax
            currBits = bin(nums[i])[2:].count('1')
            currMin = nums[i]
            currMax = nums[i]

    return currMin > prevMax

nums1 = [8,4,2,30,15]
nums2 = [1,2,3,4,5]
nums3 = [3,16,8,4,2]

print(canSortArray(nums3))