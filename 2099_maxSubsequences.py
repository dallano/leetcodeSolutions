# Solution to 2099. Find Subsequence of Length K with the Largest Sum
# You are given an integer array nums and an integer k. You want to find a subsequence of nums of length k that has the largest sum.
# Return any such subsequence as an integer array of length k.
# A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.

def maxSubsequence(nums, k):
    # First rebuild the array with memory of indices. Then sort based on original values
    numsIndex = [(val, i) for i, val in enumerate(nums)]

    # Sort in descending values
    numsIndex.sort(key=lambda x: -x[0])

    # Take top k and sort by original index
    topValues = sorted(numsIndex[:k], key=lambda x: x[1])

    # Return array without indecies
    return [num for num, index in topValues]

nums1 = [2, 1, 3, 3]
k1 = 2
nums2 = [-1, -2, 3, 4]
k2 = 3
nums3 = [3, 4, 3, 3]
k3 = 2
nums4 = [100, 54, 12, 43, 12, 99]
k4 = 3

print(maxSubsequence(nums1, k1))