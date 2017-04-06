"""Write an efficient algorithm that searches for a value in an m x n matrix. 
This matrix has the following properties:Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.For example,Consider the following matrix: [
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
Given target = 5, return true.Given target = 20, return false.
"""
def searchMatrix(m, t):
"""    :type matrix: List[List[int]]
:type target: int
:rtype: bool
"""
  if m==[]:
    return False
  r,c=0,len(m[0])-1
  while r<len(m) and c>=0:
    if m[r][c]==t:
      return True
    elif m[r][c]>t:
      c-=1
    else:
      r+=1
  return False
