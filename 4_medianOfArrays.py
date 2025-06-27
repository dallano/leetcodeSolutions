# Solution to 4. Median of Two Sorted Arrays
# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
# The overall run time complexity should be O(log (m+n)).

def findMedianSortedArrays(nums1, nums2):
    nums1.extend(nums2)
    nums1.sort()

    index = (len(nums1) // 2) # Return int index of center of the array

    # If our list has an even amount, return the average of the two middle most values
    if len(nums1) % 2 == 0:
        return (nums1[index - 1] + nums1[index]) / 2.0
    else:
        return nums1[index]
    
print(findMedianSortedArrays([1, 2], [3, 4]))