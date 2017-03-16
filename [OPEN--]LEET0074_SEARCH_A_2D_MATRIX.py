#coding=utf-8

"""
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
For example,

Consider the following matrix:

[
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
Given target = 3, return true.
"""

#due to the matrix is ascending, so we can assume to flat it as a list
#mid's index = (mid //n, mid - mid//n * n)

def searchMatrix_v0(matrix, target):
	if not matrix or not matrix[0] or matrix[0][0] > target or matrix[-1][-1] < target: return False
	left, rigth, n = 0, len(matrix)*len(matrix[0]-1), len(matrix[0])
	while left <= right:
		mid = left + int((right - left)/2)
		row = mid // n
		col = mid - row*n
		if matrix[row][col] < target: left = mid + 1
		elif matrix[row][col] > target: right = mid - 1
		else: return True
	return False


#use IN
def searchMatrix_v1(matrix, target):
	for each in matrix:
		if target in each: return True
	return False
