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