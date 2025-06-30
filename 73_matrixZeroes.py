# Solution to 73. Set Matrix Zeroes
# Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.
# You must do it in place.

# Dev notes: if a 0 is any subarray, the entire subarray becomes 0, otherwise all
# other values in that column index become 0

import copy

def setZeroes(matrix):
    col = len(matrix)
    row = len(matrix[0])

    matrixIndex = [[1 for _ in range(row)] for _ in range(col)]

    # First pass to find 0s and mark their index
    for x in range(col):
        for y in range(row):
            if matrix[x][y] == 0:
                matrixIndex[x][y] = 0

    for x in range(col):
        for y in range(row):
            if matrixIndex[x][y] == 0:
                for i in range(row): # Set entire row to 0
                    matrix[x][i] = 0
                for j in range(col): # Set entire column to 0
                    matrix[j][y] = 0
    return matrix

# Test Cases
case1 = [[1,1,1],[1,0,1],[1,1,1]]       # Solution: [[1,0,1],[0,0,0],[1,0,1]]
case2 = [[0,1,2,0],[3,4,5,2],[1,3,1,5]] # Solution: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]

print(setZeroes(case2))