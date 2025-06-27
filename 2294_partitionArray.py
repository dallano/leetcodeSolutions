# Solution to 2294. Partition Array Such That Maximum Difference is K
# You are given an integer array nums and an integer k. You may partition nums into one or more subsequences such that each
# element in nums appears in exactly one of the subsequences.
# Return the minimum number of subsequences needed such that the difference between the maximum and minimum values in each
# subsequence is at most k.
# A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.

def partitionArray(nums, k):
    max = 0

    # If we have a valid array, by default we have 1 potential parition
    if len(nums) > 0:
        nums.sort()
        max += 1
        start = nums[0]
    else:
        return max # Otherwise 0

    # Each time we increase beyond value k in a sorted array, we have a potential new parition
    for val in nums:
        if val - start > k:
            start = val
            max += 1

    return max

array = [1, 1, 1, 2, 3, 5, 6, 7, 10, 13, 17]
diff  = 3

print(partitionArray(array, diff))