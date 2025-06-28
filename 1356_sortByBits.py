# Solution to 1356. Sort Integers by the Number of 1 Bits
# You are given an integer array arr. Sort the integers in the array in ascending order by the number of 1's
# in their binary representation and in case of two or more integers have the same number of 1's you have to
# sort them in ascending order.
# Return the array after sorting it.

def sortByBits(arr):
    arr.sort() # First sort in ascending order as a base case
    arr.sort(key=lambda x: bin(x)[2:].count('1')) # Lambda function converts value into a binary string, then returns # of 1s

    return arr

nums1 = [0,1,2,3,4,5,6,7,8]
nums2 = [1024,512,256,128,64,32,16,8,4,2,1]

print(sortByBits(nums1))