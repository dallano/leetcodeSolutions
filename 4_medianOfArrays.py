def findMedianSortedArrays(nums1, nums2):
    nums1.extend(nums2)
    nums1.sort()

    index = (len(nums1) // 2)

    # If our list has an even amount, return the median of the two middle most values
    if len(nums1) % 2 == 0:
        return (nums1[index - 1] + nums1[index]) / 2.0
    else:
        return nums1[index]
    
print(findMedianSortedArrays([1, 2], [3, 4]))