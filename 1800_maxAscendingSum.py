# Solution to 1800. Maximum Ascending Subarray sum
# Given an array of positive integers nums, return the maximum possible sum of an strictly increasing subarray in nums.
# A subarray is defined as a contiguous sequence of numbers in an array.

def maxAscendingSum(nums):
    maxSum  = nums[0]
    currSum = nums[0]

    for i in range(1, len(nums)):
        print("Current: ", nums[i], "Previous: ", nums[i-1])
        if nums[i] > nums[i - 1]:
            currSum += nums[i]
            if currSum > maxSum:
                maxSum = currSum
        else:
            currSum = nums[i]

    return maxSum

# Test cases:
nums1 = [10, 20, 30, 5, 10, 50] # Solution 65
nums2 = [10, 20, 30, 40, 50] # Solution 150
nums3 = [12, 17, 15, 13, 10, 11, 12] # Solution 33
nums4 = [300, 100, 190] # Solution 300
nums5 = [100, 101, 102, 100, 600, 200, 202] # Solution 700

print(maxAscendingSum(nums5))